# Generated by Django 4.1.7 on 2023-05-03 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ignite', '0011_alter_student_id_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='select_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ignite.student')),
            ],
        ),
    ]
