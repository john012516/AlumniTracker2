# Generated by Django 3.1.7 on 2022-03-10 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0031_useremployed_alumni'),
    ]

    operations = [
        migrations.AddField(
            model_name='userselfemployed',
            name='alumni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CITAT.alumni'),
        ),
        migrations.AddField(
            model_name='userunemployed',
            name='alumni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CITAT.alumni'),
        ),
    ]
