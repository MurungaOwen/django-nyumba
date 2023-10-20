from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.utils.translation import gettext_lazy as _#kusaidia in translation
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class CustomUser(AbstractUser):#leaving username and first name 
    username=None
    email=models.EmailField(_("enter your email"),unique=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    phone_number=PhoneNumberField(blank=True)
    is_tenant=models.BooleanField(default=False)
    profile_picture=models.ImageField(upload_to="user_profiles",null=True,blank=True)
    #
    #-------other user details------->
    objects=CustomUserManager()

# class Tenant(models.Model):
#     contact=models.TextField()
#     first_name=models.TextField()
#     last_name=models.TextField()



