# Generated by Django 5.0.6 on 2024-07-17 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0026_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$HPNiaRYO1RTC12851RsZn2$s9WIS0urDMBq5Somwt6LvyCDY8XIQI5cg6c9Gq73/Cs=', max_length=128),
        ),
    ]
