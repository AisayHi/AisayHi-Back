# Generated by Django 5.0.6 on 2024-09-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$BFxNcym3yEnPvf4dlvQ8Lb$O3WdmWD4a9pMUOhG4+sv+GqjdUeJa6lf/ze6PE++caM=', max_length=128),
        ),
    ]
