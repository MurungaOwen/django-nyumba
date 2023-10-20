from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/",include("usersapp.urls")),
    path("",include("core.urls")),

    #----------------------kusahau password--------------------
    path("reset-password/",PasswordResetView.as_view(html_email_template_name="password_reset_email.html"),name="password_reset"),#enter your email form
    path("reset-password-done/",PasswordResetDoneView.as_view(),name="password_reset_done"),#we have emailed you instructs and stuff
    path("reset-password-confirm/<uidb64>/<token>/",PasswordResetConfirmView.as_view(success_url="/users/login"),name="password_reset_confirm"),#clck email
    path("reset-password-complete/", PasswordResetCompleteView.as_view(template_name="new_password.html"),name="password_reset_complete"),#new passwd entered...login now

    #----------kuchange password---------------------------------
    path("change-password/",PasswordChangeView.as_view(),name="password_change"),
    path("change-password-done/",PasswordChangeDoneView.as_view(),name="password_change_done")

]
#-serving images and files
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

