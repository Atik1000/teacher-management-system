# Generated by Django 5.0 on 2024-07-10 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seatplan', '0007_student_seatplan'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seatplan',
            unique_together={('room', 'seat_number')},
        ),
        migrations.RemoveField(
            model_name='seatplan',
            name='column',
        ),
    ]