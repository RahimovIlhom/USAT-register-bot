# Generated by Django 5.0.2 on 2024-03-01 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_alter_testresult_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_app.test'),
        ),
    ]
