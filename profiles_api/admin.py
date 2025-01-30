from django.contrib import admin

# Register your models here.
from profiles_api import models

admin.site.register(models.UserProfile) # Tells django admin to register our userprofile model with the admin site. 

