from django.contrib.auth.models import User
from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework_jwt.settings import api_settings

def jwt_response_handler(token, user=None, request=None):

    payload = {
        'token': token,
        'user_id': user.id,
        'email': user.email,
        'username': user.username
        # Add any other user-related data you want to include
    }
    api_settings.JWT_RESPONSE_PAYLOAD_HANDLER(payload, user, request)

    return payload