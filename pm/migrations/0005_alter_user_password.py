# Generated by Django 5.0.6 on 2024-09-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0004_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$r6a4UtfwgNYD0uggUJ7U6s$XSBHBmcPe4sR0pUl1oYsh6Yot0eCJthyuYBZFV68Sj8=', max_length=128),
        ),
    ]
