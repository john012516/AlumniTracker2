# Generated by Django 3.1.7 on 2022-04-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0079_companyphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyphoto',
            name='Company_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='companyphoto',
            name='Company_zipcode',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='companyphoto',
            name='Income',
            field=models.CharField(choices=[('10,000-20,000', '10,000-20,000'), ('20,000-30,000', '20,000-30,000'), ('30,000-40,000', '30,000-40,000'), ('50,000-70,000', '40,000-50,000'), ('70,000-80,000', '70,000-80,000'), ('80,000-90,000', '80,000-90,000'), ('90,000-100,000', '90,000-100,000')], max_length=200, null=True),
        ),
    ]
