# Generated by Django 3.2.5 on 2022-04-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0083_merge_0073_carausel_0082_auto_20220406_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_Telephone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]