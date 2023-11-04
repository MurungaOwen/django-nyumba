from django.urls import path

from. import views
app_name="usersapp"
urlpatterns = [
    #path(),
    path("register/",views.register_user,name="signup"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("verify/<uidb64>/<token>/",views.email_account_activation_token,name="activate_account")
]

