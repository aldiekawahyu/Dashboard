# Generated by Django 5.0.1 on 2024-03-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_page', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
