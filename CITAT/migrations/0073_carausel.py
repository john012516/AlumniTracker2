# Generated by Django 4.0.2 on 2022-03-31 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0072_alter_alumni_country_alter_alumni_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carausel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics/%y/%m/%d/')),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(max_length=100)),
            ],
        ),
    ]
