# Generated by Django 5.0.1 on 2024-01-31 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.CharField(max_length=20, unique=True)),
                ('language', models.CharField(max_length=10)),
                ('fullname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('school_number', models.CharField(max_length=20)),
                ('science', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
