from django import forms
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class RegisterForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={
        "class":"form-control",
        "placeholder":"enter your email"
    }))
    phone_number=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"enter your number"
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"enter password "
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"confirm your password"
    }))

    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("passwords dont match")
        elif len(password2)<7:
            raise forms.ValidationError("password is too short")
        else:
            return password2

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("account with such email exists try login")
        return email

class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        "class":"form-control",
        "placeholder":"enter your email"
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"enter password"
    }))

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if  not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("no such email registered signup instead")
        return email

