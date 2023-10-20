from django.contrib import admin
from .models import Houses
# Register your models here.

@admin.register(Houses)
class HousesAdmin(admin.ModelAdmin):
    list_display=["house_make","uploaded_time","bedrooms"]
    

