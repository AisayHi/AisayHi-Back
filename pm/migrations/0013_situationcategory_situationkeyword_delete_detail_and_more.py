# Generated by Django 5.0.6 on 2024-09-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0012_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='SituationCategory',
            fields=[
                ('categoryKey', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'situation_category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SituationKeyword',
            fields=[
                ('keywordKey', models.AutoField(primary_key=True, serialize=False)),
                ('keyword', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'situation_keyword',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='situation',
            options={'managed': True},
        ),
    ]
