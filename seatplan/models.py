from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.roll_no} - {self.name}'

class Room(models.Model):
    room_no = models.IntegerField()
    number_of_seats = models.IntegerField()
    
    def __str__(self):
        return f'Room {self.room_no}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Ensure columns are created on room creation
        self.create_columns()

    def create_columns(self):
        Column.objects.filter(room=self).delete()  # Remove existing columns
        number_of_columns = self.number_of_seats // 3
        for i in range(1, number_of_columns + 1):
            intake = Intake.objects.create(name=f'Intake {i}')
            Column.objects.create(room=self, intake=intake, roll=f'Roll {i}')

class Intake(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Column(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
    roll = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.room} - {self.intake.name} - {self.roll}'
