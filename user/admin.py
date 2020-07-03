from django.contrib import admin
from .models import CustomUser, UserProfile, AddressGlobal

# Register your models here.
admin.site.register((CustomUser, UserProfile, AddressGlobal, ))
