# Generated by Django 2.1.5 on 2019-02-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_remove_transaction_debit_or_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='remarks',
            field=models.CharField(default=None, max_length=90, null=True),
        ),
    ]
