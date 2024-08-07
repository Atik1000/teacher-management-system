# Generated by Django 5.0 on 2024-07-10 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatplan', '0004_alter_room_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='columns',
            new_name='num_columns',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='seats',
            new_name='num_seats',
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='seatplan',
            unique_together={('room', 'column', 'seat_number')},
        ),
    ]
