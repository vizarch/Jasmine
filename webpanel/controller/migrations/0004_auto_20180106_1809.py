# Generated by Django 2.0 on 2018-01-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0003_task_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='parameters',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='results',
            field=models.TextField(blank=True, null=True),
        ),
    ]
