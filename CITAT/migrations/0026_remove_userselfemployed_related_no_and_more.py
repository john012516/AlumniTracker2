# Generated by Django 4.0.2 on 2022-03-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0025_remove_userunemployed_consider_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userselfemployed',
            name='related_no',
        ),
        migrations.RemoveField(
            model_name='userselfemployed',
            name='related_yes',
        ),
        migrations.AddField(
            model_name='userselfemployed',
            name='related',
            field=models.CharField(max_length=50, null=True),
        ),
    ]