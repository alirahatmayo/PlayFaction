# Generated by Django 2.1.5 on 2019-02-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='debit_or_credit',
            field=models.CharField(choices=[('d', 'Debit'), ('c', 'Credit')], max_length=1, null=True),
        ),
    ]