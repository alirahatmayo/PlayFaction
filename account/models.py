from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from game.models import Game
import datetime
from django.utils import timezone
from decimal import Decimal



#
# class UserProfileQuerySet(models.QuerySet):
#     pass
#
# class UserProfileManager(models.Manager):
#     def get_queryset(self):
#         return UserProfileQuerySet(self.model, using=self._db)

class Account(models.Model):


    TRANSACTION_CHOICES = (
        ('tu', 'TopUp'),
        ('gf', 'Game Fee'),
        ('wd', 'Withdrawal'),
    )
    DEBIT_CREDIT_CHOICES = (
        ('d', 'Debit'),
        ('c', 'Credit')
    )

    account_title = models.OneToOneField(User, on_delete=models.CASCADE)
    # account_title = models.OneToOneField(User.username, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)
    remarks = models.CharField(max_length=90, default=None)




    def __str__(self):
        return str(self.account_title)[:50]

    @property
    def transactions(self):
        return self.transfer_from_set.all()



