from django.contrib import admin
from .models import UserProfile
# from .forms import StatusForm

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'birth_date', 'gender', 'phone_no']

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)

