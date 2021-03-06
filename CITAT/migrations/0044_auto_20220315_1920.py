# Generated by Django 3.1.7 on 2022-03-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0043_auto_20220315_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='Citizenship',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='Civil',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='Dob',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='Pob',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='Religion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='Telephone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='address2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='contactnumber',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='incaseofemergency',
            field=models.CharField(editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='nameofemergency',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='relation',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='employed',
            field=models.CharField(choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed')], max_length=200, null=True),
        ),
    ]
