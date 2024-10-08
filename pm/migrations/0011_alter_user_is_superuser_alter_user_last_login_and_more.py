# Generated by Django 5.0.6 on 2024-09-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0010_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
