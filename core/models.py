from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
# Create your models here.
User=get_user_model()
class Houses(models.Model):
    house_type=(
        ("bedsitter","bedsitter"),
        ("mansion","mansion"),
        ("villa","villa"),
        ("bungalow","bungalow")
    )
    uploaded_time=models.DateTimeField(auto_now_add=True)
    image_1=models.ImageField(null=True,blank=True,upload_to="house_images")
    image_2=models.ImageField(null=True,blank=True,upload_to="house_images")
    image_3=models.ImageField(null=True,blank=True,upload_to="house_images")
    location=models.TextField()
    house_make=models.CharField(max_length=20,choices=house_type)
    bedrooms=models.IntegerField()
    uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE)
    price_per_month=models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        verbose_name_plural="houses"
        ordering=["uploaded_time"]

