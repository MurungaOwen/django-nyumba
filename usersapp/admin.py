from django.contrib import admin

#----get all my models and register them here---->
from .models import (CustomUser,
                     HouseAgent)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=["id","email","is_staff"] #--->how the info will be shown in the admin panel

    
@admin.register(HouseAgent)
class HouseAgentAdmin(admin.ModelAdmin):
    pass

