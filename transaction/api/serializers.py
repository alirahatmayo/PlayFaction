from rest_framework import serializers
from transaction.models import Transaction
from transaction import exceptions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from account.models import Account


'''
Serializer -> converts into JSON
Serializer ->does Validations on data
'''


class TransactionSerializer(serializers.ModelSerializer):

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

    def validate(self, data):
        sender = data.get("sender")
        receiver=data.get("receiver")
        amount=data.get("amount")
        transfer_type = data.get("transfer_type")
        remarks=data.get("remarks")

        # if not (sender == receiver):

        get_sender = User.objects.get(username = sender)
        sender_id = get_sender.id
        transfer_from = Account.objects.get(account_title=sender_id)
        balance = transfer_from.balance
        get_receiver = User.objects.get(username = receiver)
        receiver_id = get_receiver.id
        transfer_to = Account.objects.get(account_title=receiver_id)
        # else:
        # raise serializers.ValidationError("user must be authenticated to perform transfer")

        if not(sender == receiver):
            if balance < amount:
                msg = "Unable to debit %.2f from account of %s:"
                raise serializers.ValidationError(
                msg % (amount, sender))
            elif amount < 20 :
                msg = "you can not transfer ammount value less than 20 : "
                raise serializers.ValidationError(msg)
            elif remarks == "":
                msg = "ammount of %.2f has been transfered from %s, to %s :"
                remarks = msg%(amount, sender, receiver)
            else:
                return data
        else:
            raise serializers.ValidationError("You can not transfer funds to yourself!!")



    def create(self, validated_data):

        #minus the ammount from sender
        amount = validated_data.get('amount')
        sender = validated_data.get('sender')
        get_sender = User.objects.get(username=sender)
        sender_id = get_sender.id
        transfer_from = Account.objects.get(account_title=sender_id)
        balance = transfer_from.balance
        balance -=amount
        transfer_from.balance = balance
        transfer_from.save()

        #plus the amount in receiver
        receiver = validated_data.get('receiver')
        get_receiver = User.objects.get(username=receiver)
        receiver_id = get_receiver.id
        transfer_to = Account.objects.get(account_title=receiver_id)
        balance = transfer_to.balance
        balance += amount
        transfer_to.balance = balance
        transfer_to.save()

        return Transaction.objects.create(**validated_data)