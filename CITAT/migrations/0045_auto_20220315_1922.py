# Generated by Django 3.1.7 on 2022-03-15 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0044_auto_20220315_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumni',
            old_name='Dob',
            new_name='Date_of_Birth',
        ),
        migrations.RenameField(
            model_name='alumni',
            old_name='Pob',
            new_name='Place_of_Birth',
        ),
    ]
