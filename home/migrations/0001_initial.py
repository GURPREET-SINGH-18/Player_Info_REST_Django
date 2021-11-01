# Generated by Django 3.2.4 on 2021-10-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=40)),
                ('nationality', models.CharField(max_length=40)),
                ('born', models.CharField(max_length=40)),
                ('birthplace', models.CharField(max_length=40)),
                ('height', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=40)),
                ('batting_style', models.CharField(max_length=40)),
                ('bowling_style', models.CharField(max_length=40)),
                ('teams', models.TextField(max_length=1000)),
                ('total_ing', models.IntegerField()),
                ('total_run', models.IntegerField()),
                ('total_hun', models.IntegerField()),
                ('total_fif', models.IntegerField()),
                ('total_bowling_ing', models.IntegerField()),
                ('total_wicket', models.IntegerField()),
                ('total_economy', models.FloatField()),
                ('total_avg', models.FloatField()),
                ('small_info', models.TextField(max_length=1000)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]