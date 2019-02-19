from django.contrib import admin
from.models import Transaction

# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'sender', 'receiver' , 'amount', 'transaction_type', 'transaction_time', 'remarks',  ]


#
# account = models.ForeignKey(settings.AUTH_USER_MODEL  , on_delete=models.PROTECT) #protect so it will keep in database anyways
#     counterparty = models.ForeignKey(User, on_delete=models.PROTECT)
#     debit_or_credit = models.CharField(choices=DEBIT_CREDIT_CHOICES, max_length=1, null= True)
#     ammount = models.FloatField(default=0.0)
#     transaction_type = models.CharField(max_length=2, choices=TRANSACTION_CHOICES, null=True)
#     transaction_time = models.DateTimeField(default=datetime.datetime.now, timezone= timezone().now )
#     remarks = models.CharField(max_length=90, default=None)


admin.site.register( Transaction, TransactionAdmin)