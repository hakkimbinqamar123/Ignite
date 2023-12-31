# Generated by Django 4.1.1 on 2023-04-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ignite', '0006_event_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ImageField(default=0, upload_to='images'),
        ),
        migrations.AddField(
            model_name='student',
            name='college',
            field=models.CharField(default=0, max_length=100, verbose_name='college'),
        ),
        migrations.AddField(
            model_name='student',
            name='events',
            field=models.CharField(default=0, max_length=100, verbose_name='events'),
        ),
        migrations.AddField(
            model_name='student',
            name='id_card',
            field=models.ImageField(default=0, upload_to='images'),
        ),
    ]
