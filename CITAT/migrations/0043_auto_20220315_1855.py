# Generated by Django 3.1.7 on 2022-03-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0042_alumni_employed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='employed',
            field=models.CharField(choices=[('employed', 'employed'), ('unemployed', 'unemployed')], max_length=200, null=True),
        ),
    ]
