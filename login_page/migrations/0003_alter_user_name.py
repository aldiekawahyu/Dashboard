# Generated by Django 5.0.1 on 2024-03-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_page', '0002_remove_user_email_user_name_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
    ]
