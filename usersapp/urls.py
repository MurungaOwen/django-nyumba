from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView
)
from. import views
app_name="usersapp"
urlpatterns = [
    #path(),
    path("register/",views.register_user,name="signup"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("verify/<uidb64>/<token>/",views.account_activation_token,name="activate_email"),


    #----------------------kusahau password--------------------
    path("reset-password/",PasswordResetView.as_view()),#enter your email form
    path("reset-password-done/",PasswordResetDoneView.as_view()),#we have emailed you instructs and stuff
    path("reset-password-confirm/<uidb64>/<token>/",PasswordResetConfirmView.as_view()),#clck email
    path("reset-password-complete/", PasswordResetCompleteView.as_view()),#new passwd entered

    #----------kuchange password---------------------------------
    path("change-password/",PasswordChangeView.as_view()),
    path("change-password-done/",PasswordChangeDoneView.as_view())

]

