# Generated by Django 3.1.7 on 2022-03-17 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0053_auto_20220317_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='employed',
            name='alumni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CITAT.alumni'),
        ),
    ]