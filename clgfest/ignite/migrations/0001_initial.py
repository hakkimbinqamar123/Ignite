# Generated by Django 4.1.1 on 2023-02-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Judges',
            fields=[
                ('j_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id of user')),
                ('username', models.CharField(max_length=50, verbose_name='Name of user')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.IntegerField(verbose_name='Phone number')),
                ('password', models.CharField(max_length=25, verbose_name='Password')),
                ('qualification', models.CharField(max_length=25, verbose_name='Usertype')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('candidate_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id of user')),
                ('username', models.CharField(max_length=50, verbose_name='Name of user')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.IntegerField(verbose_name='Phone number')),
                ('password', models.CharField(max_length=25, verbose_name='Password')),
            ],
        ),
    ]
