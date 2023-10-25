from django.contrib.auth.base_user import BaseUserManager

class BaseUserManager(BaseUserManager):

    def create_user(self, email , password = None , **extra_fields):
        if not email:
            raise ValueError("Email is Required")
        
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(email = email , **extra_fields)
        user.set_password(password)
        user.save(using = self.db)

    def create_superuser(self, email , role , password = None , **extra_fields ):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('role',"Admin")
        
        return self.create_user(email = email , password=password, **extra_fields)