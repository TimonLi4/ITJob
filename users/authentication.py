from typing import Any
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest
from django.contrib.auth import get_user_model

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username, password, **kwargs):
        user_model=get_user_model()
        try:
            user=user_model.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None
        
    
    def get_user(sefl,user_id):
        user_model=get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None

