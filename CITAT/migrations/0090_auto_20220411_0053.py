# Generated by Django 3.2.5 on 2022-04-10 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0089_auto_20220411_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_Telephone',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_phone',
        ),
    ]
