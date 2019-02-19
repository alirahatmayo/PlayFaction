from rest_framework import serializers
from transaction.models import Transaction
from transaction import exceptions
from rest_framework.response import Response
from rest_framework import status

from account.models import Account

'''
Serializer -> converts into JSON
Serializer ->does Validations on data
'''

class TransactionSerializer(serializers.ModelSerializer):

    # def validate(self, data):
    #     sender = data.get("sender")
    #     receiver=data.get("receiver")
    #     amount=data.get("amount")
    #     transfer_type = data.get("transfer_type")
    #     remarks=data.get("remarks")
    #
    #     # if not (sender == receiver):
    #     transfer_from = Account.objects.get(account_title_id=sender)
    #     balance = transfer_from.balance
    #     transfer_to = Account.objects.get(account_title_id=receiver)
    #     # else:
    #     # raise serializers.ValidationError("user must be authenticated to perform transfer")
    #
    #     if balance < amount:
    #         msg = "Unable to debit %.2f from account of %s:"
    #         raise serializers.ValidationError(
    #         msg % (amount, sender))
    #     elif amount < 20 :
    #         msg = "you can not transfer ammount value less than 20 : "
    #         raise serializers.ValidationError(msg)
    #     elif remarks =="":
    #         remarks = None
    #     else:
    #         return data


    class Meta:
        model = Transaction
        fields = [
            'sender',
            'receiver',
            'amount',
            'transaction_type',
            'transaction_time',
            'remarks',
        ]
    read_only_fields = ['user']



        # else:
        #     raise serializers.ValidationError("you can not transfer fund to yourself!!")
    # def after_transaction(self,data):

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # def create(self, validated_data):
    #     # sender = validated_data.pop('sender')
    #     # receiver = validated_data.pop('receiver')
    #     # amount = validated_data.pop('amount')
    #     # remarks = validated_data.pop('remarks', None)
    #     # transaction_type = validated_data.pop('transaction_type', None)
    #     trans = Transaction.objects.get_or_create(**validated_data)
    #     serializer = TransactionSerializer(data=validated_data, many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #     else:
    #         raise serializers.ValidationError(serializer.errors)
    #     return trans
    #     # return super().create(request)
    #     # update_accounts(sender, receiver, amount)
    #     # sender_acc = Account.objects.get(account_title_id=sender)
    #     # sender_acc.balance -= amount
    #     # # if transaction.is_valid():
    #     # sender_acc.save()
    #     #
    #     # receiver_acc = Account.objects.get(account_title_id=receiver)
    #     # receiver_acc.balance += amount
    #     # # if transaction.is_valid():
    #     # receiver_acc.save()
    #
    # # def update_accounts(self, sender, receiver, amount):
    # #     sender_acc = Account.objects.get(account_title_id=sender)
    # #     sender_acc.balance -= amount
    # #     sender_acc.save()
    # #
    # #     receiver_acc = Account.objects.get(account_title_id=receiver)
    # #     receiver_acc.balance += amount
    # #     receiver_acc.save()



