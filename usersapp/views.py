from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.template.loader import render_to_string#convert email in html to string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site#returns like the domain and stuff
from django.utils.html import strip_tags
from django.utils.encoding import force_bytes,force_str
# Create your views here.
from .forms import RegisterForm,LoginForm
from .tokens import email_token_generator
User=get_user_model()

def register_user(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        password1=form.cleaned_data.get("password1")
        email=form.cleaned_data.get("email")
        phone_number=form.cleaned_data.get("phone_number")
        user=User(email=email,phone_number=phone_number)
        user.set_password(password1)
        user.is_active=False
        user.save()
        print(email)
        send_account_activation_email(request,user,email)#----calling function ya   kutuma email-------
        messages.success(request,"user created ,check mail to activate eaccount")
        return redirect("usersapp:login")
    return render(request,"signup.html",locals())

#----------------inakam kwa the email template-----------------------
def send_account_activation_email(request,user,to_email):
    mail_subject="account activation"
    html_message=render_to_string(
        "activate_account.html",{
            "user":to_email,
            "site":get_current_site(request).domain,
            "token":email_token_generator(user),
            "uid":urlsafe_base64_encode(force_bytes(user.pk))
        })
    plain_message=strip_tags(html_message)
    if send_mail(mail_subject,plain_message,"admin@nyumba.com",[to_email],html_message):
        messages.info(request,"check mail inbox to activate account or the spam folder")
    else:
        messages.error(request,"unable to send mail")
    return redirect("usersapp:login")
    
#-------------------ukiclick link from the email------------
def account_activation_token(request,uidb64,token):
    uid=force_str(urlsafe_base64_decode(uidb64))
    user=User.object.get(pk=uid)
    if email_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,"account activated")
        return redirect("home")
    else:
        messages.error(request,"the token expired,request a new password change")


def login_user(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        email=form.cleaned_data.get("email")
        password=form.cleaned_data.get("password")
        user=authenticate(
            email=email,password=password
        )
        if user:
            login(request,user)
            print("login")
            messages.success(request,f"logged in as ${email}")
            return redirect("home")
            
        else:
            messages.info(request,"check password and try again")
    return render(request,"login.html",locals())

def logout_user(request):
    logout(request)#####close the session ama kulogout a user
    return redirect("home")


