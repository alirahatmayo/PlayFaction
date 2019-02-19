from rest_framework import serializers
from transaction.api.serializers import TransactionSerializer
from account.models import Account

'''
Serializer -> converts into JSON
Serializer ->does Validations on data
'''


class AccountSerializer(serializers.ModelSerializer):
    transfer_from = TransactionSerializer(many= True)
    transfer_to = TransactionSerializer(many= True)

    class Meta:
        model = Account
        fields = [
            'id',
            'account_title',
            'balance',
            'remarks',
            'transfer_from',
            'transfer_to'

        ]
    read_only_fields = ['id']



    # def after_transaction_balance(self, amount, sender, receiver):
    #     sender_person = Account.objects.filter(user_id=sender)
    #     sender_balance =
    #     sender_balance
    #     receiver_balance = Account.objects.filter(user_id=receiver)

