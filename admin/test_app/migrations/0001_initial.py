# Generated by Django 5.0.2 on 2024-02-11 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('science', models.CharField(max_length=20)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('time_continue', models.IntegerField()),
                ('questions_count', models.IntegerField(default=10)),
            ],
            options={
                'db_table': 'tests',
            },
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_question', models.IntegerField(null=True)),
                ('question_uz', models.CharField(max_length=500)),
                ('question_ru', models.CharField(max_length=500)),
                ('true_response', models.IntegerField()),
                ('test', models.ManyToManyField(related_name='test_questions', to='test_app.test')),
            ],
            options={
                'db_table': 'test_questions',
            },
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.CharField(max_length=20, unique=True)),
                ('language', models.CharField(max_length=10)),
                ('fullname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('region', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('school_number', models.CharField(max_length=20)),
                ('science', models.CharField(max_length=20)),
                ('responses', models.CharField(max_length=50)),
                ('result_time', models.DateTimeField(auto_now_add=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.test')),
            ],
            options={
                'db_table': 'test_result',
            },
        ),
    ]
