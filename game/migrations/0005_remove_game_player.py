# Generated by Django 2.1.5 on 2019-02-10 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20190210_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='player',
        ),
    ]
