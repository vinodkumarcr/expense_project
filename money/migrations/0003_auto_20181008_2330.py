# Generated by Django 2.0.2 on 2018-10-08 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0002_auto_20181008_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='totals',
            old_name='Friends_share',
            new_name='Final_amount',
        ),
        migrations.RemoveField(
            model_name='totals',
            name='My_share',
        ),
        migrations.RemoveField(
            model_name='totals',
            name='Total_money',
        ),
    ]
