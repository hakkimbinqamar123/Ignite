# Generated by Django 4.1.1 on 2023-05-08 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ignite', '0019_delete_venue_remove_event_venue_id_event_venue_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
