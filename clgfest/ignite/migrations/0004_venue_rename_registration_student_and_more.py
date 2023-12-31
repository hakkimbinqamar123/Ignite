# Generated by Django 4.1.1 on 2023-02-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ignite', '0003_rename_events_event_rename_judges_judge_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venue_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id of stage')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('block', models.IntegerField(verbose_name='block')),
            ],
        ),
        migrations.RenameModel(
            old_name='Registration',
            new_name='Student',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='stage_id',
            new_name='venue_id',
        ),
    ]
