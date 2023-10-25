from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from rest_framework.views import APIView
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework import status
from django.contrib.auth import get_user_model
from knox.views import LogoutView



from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer 

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *
from .forms import *
from django.http import JsonResponse
from rest_framework_jwt.views import obtain_jwt_token
from django.http import HttpRequest



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib.auth.models import User
from .serializers import UserSerializer


# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def task(request):
    if (request.user.is_superuser):
        task = Task.objects.all()
    else:
        task = Task.objects.filter(user = request.user)

    return render(request, 'task.html', {'task':task})
def add_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('task')

    return render(request, 'add_task.html', {'form':form})


def update_task(request,id):
    item = get_object_or_404(Task, pk=id)
    

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            
            return redirect('task')  # Redirect to the list view
    else:
        form = TaskForm(instance=item)

    return render(request, 'update.html', {'form': form})


def delete_task(request,id):
    
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return JsonResponse({'message': "deleted"})
    




def profile(request):
    return render(request, 'profile.html')

class CustomLogoutView(LogoutView):
    template_name = 'home.html'



# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

import json
@api_view(['POST'])
def signup(request):
    
    
    data = json.loads(request.body)  # Parse the JSON data sent by the client
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    print(username , email, password, "<-----")
    
    if not username or not password:
        return Response({'error': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.create_user(username=username,email=email, password=password)
    except Exception as e:
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return Response({'token': token})




from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username , password , "kkkkkkkkkkkkkkkkkkkk")
        # user = authenticate(username=username, password=password)
        try : 
            user = CustomUser.objects.filter(email = username).first()
        except Exception as e:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if user:
            login(request , user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            print(access_token)
            return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
