# Generated by Django 3.0.7 on 2020-11-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201105_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle_info',
            old_name='vehicle_name',
            new_name='vehicle_type',
        ),
        migrations.RemoveField(
            model_name='points',
            name='dropping_point3',
        ),
        migrations.RemoveField(
            model_name='points',
            name='dropping_point4',
        ),
        migrations.RemoveField(
            model_name='points',
            name='dropping_point5',
        ),
        migrations.RemoveField(
            model_name='vehicle_info',
            name='no_of_tickets',
        ),
        migrations.AddField(
            model_name='vehicle_info',
            name='bus_no',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='vehicle_info',
            name='no_of_seats',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
