# Generated by Django 5.0 on 2024-07-10 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatplan', '0002_remove_column_roll_column_column_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='column',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='student',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='number_of_columns',
            new_name='columns',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='number_of_seats',
            new_name='seats',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll_no',
        ),
        migrations.AddField(
            model_name='room',
            name='number',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='intake',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seatplan.intake'),
        ),
        migrations.CreateModel(
            name='SeatPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.IntegerField()),
                ('seat_number', models.IntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seatplan.room')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seatplan.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Column',
        ),
        migrations.DeleteModel(
            name='Seat',
        ),
    ]
