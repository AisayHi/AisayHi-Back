# Generated by Django 5.0.6 on 2024-09-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0011_alter_user_is_superuser_alter_user_last_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
