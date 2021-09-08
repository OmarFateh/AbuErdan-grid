# Generated by Django 2.2.19 on 2021-09-07 21:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20210907_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('avg_temperature', models.FloatField(verbose_name='Average Temperature')),
                ('avg_humidity', models.FloatField(verbose_name='Average Humidity')),
                ('start_date', models.DateField(verbose_name='Date of first record of the 10 records')),
                ('end_date', models.DateField(verbose_name='Date of last record of the 10 records')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField(validators=[django.core.validators.MinValueValidator(19.0), django.core.validators.MaxValueValidator(28.0)])),
                ('humidity', models.FloatField(validators=[django.core.validators.MinValueValidator(35.0), django.core.validators.MaxValueValidator(65.0)])),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]
