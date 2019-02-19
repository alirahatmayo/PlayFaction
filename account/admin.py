from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['id','__str__' , 'balance', 'remarks']

# Register your models here.
admin.site.register(Account, AccountAdmin)