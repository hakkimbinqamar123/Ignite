# Generated by Django 4.1.1 on 2023-04-09 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ignite', '0008_alter_student_college_alter_student_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='events',
        ),
    ]
