from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime
from account.models import Account
from django.utils import timezone
from decimal import Decimal
from transaction import exceptions
from django.db import transaction



#
# class UserProfileQuerySet(models.QuerySet):
#     pass
#
# class UserProfileManager(models.Manager):
#     def get_queryset(self):
#         return UserProfileQuerySet(self.model, using=self._db)

class TransactionManager(models.Manager):
    """
    Custom manager to provide a new 'create' method to create a new transfer.
    Apparently, finance people refer to "posting a transaction"; hence why this
    """

'''
    @transaction.atomic
    def create(self, sender, receiver, amount, transaction_type, remarks=None):
        # Write out transfer (which involves multiple writes).  We use a
        # database transaction to ensure that all get written out correctly.
        self.verify_transfer(sender, receiver, amount)
        transfer = self.get_queryset().create(
            sender=sender,
            receiver=receiver,
            amount=amount,
                # user=user,
            remarks=remarks,
        transaction_type = transaction_type)
            # Create transaction records for audit trail
        Transaction.objects.create(
            sender=sender, amount=-amount, transaction_type = 'tr', remarks = 'remarks',receiver=receiver)
        Transaction.objects.create(
            receiver=receiver, amount=amount, transaction_type = 'tr',remarks = 'remarks', sender=sender)
        # Update the cached balances on the accounts
        sender.save()
        receiver.save()
        return self._wrap(transfer)

    def _wrap(self, obj):
        # Dumb method that is here only so that it can be mocked to test the
        # transaction behaviour.
        return obj

    def verify_transfer(self, sender, receiver, amount): #add friendship relation to restrict user from transfering fund to people who are not friends.
        """
        Test whether the proposed transaction is permitted.  Raise an exception
        if not.
        """

        # if amount <= 0:
        #     raise exceptions.InvalidAmount("Debits must use a positive amount")
        # if not sender.is_open():
        #     raise exceptions.ClosedAccount("Source account has been closed")
        # if not sender.can_be_authorised_by(user):
        #     raise exceptions.AccountException(
        #         "This user is not authorised to make transfers from "
        #         "this account")
        # if not receiver.is_open():
        #     raise exceptions.ClosedAccount(
        #         "Destination account has been closed")
        if sender.account.balance < amount:
        # if not sender.is_debit_permitted(amount):
            msg = "Unable to debit %.2f from account #%d:"
            raise exceptions.InsufficientFunds(
                msg % (amount, sender.id))

'''


class Transaction(models.Model):


    TRANSACTION_CHOICES = (
        ('tu', 'TopUp'),
        ('gf', 'Game Fee'),
        ('wd', 'Withdrawal'),
        ('tr', 'transfer')
    )
    DEBIT_CREDIT_CHOICES = (
        ('d', 'Debit'),
        ('c', 'Credit')
    )
    # account_title = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # amount = models.DateField(null=True)
    # debit_credit = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    # transaction_type = PhoneNumberField(blank=True)
    # transaction_no = UserProfileManager()
    # transaction_time = models.ManyToManyField(Game, blank=True, related_name='games')

    sender = models.ForeignKey(Account  , on_delete=models.PROTECT, related_name='transfer_from') #protect so it will keep in database anyways
    receiver = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, related_name='transfer_to')
    # debit_or_credit = models.CharField(choices=DEBIT_CREDIT_CHOICES, max_length=1, null= True)
    amount = models.FloatField(default=0.0)
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_CHOICES, default='tr')
    transaction_time = models.DateTimeField(default=datetime.datetime.now )
    remarks = models.CharField(max_length=90, default=None)


    # transaction_method_name = models.CharField(max_length=45,default=None)
    # transaction_method_record_unique_id = models.CharField(max_length=200)
    # transaction_amount = models.FloatField(default=0.0)
    # expiry_time_of_credited_amount = models.DateTimeField(
    #     default=datetime.datetime(year=2030, month=1, day=1, hour=00, minute=00, second=00), blank=True)
    # wallet_debit_record2wallet_credit_record = models.ForeignKey('self', default=None, null=True)
    # wallet2store_details = models.BigIntegerField(default=0)
    # hmac_or_checksum = models.CharField(max_length=200, default='temp_HMAC', blank=True, null=True)
    # is_deleted = models.CharField(max_length=45)
    objects = TransactionManager()

    def __str__(self):
        return str(self.id)[:50]


    #
    # def make_transactions(self, sender):
    #     sender =

