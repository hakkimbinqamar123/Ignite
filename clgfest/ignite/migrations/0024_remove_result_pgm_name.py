# Generated by Django 4.1.1 on 2023-05-25 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ignite', '0023_result_pgm_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='pgm_name',
        ),
    ]
