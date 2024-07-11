# models.py
from django.db import models

class Room(models.Model):
    number = models.IntegerField(unique=True)
    num_seats = models.IntegerField(default=40)
    num_columns = models.IntegerField(default=4)
    
    def __str__(self):
        return f'Room {self.number}'

class Intake(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField(unique=True)
    intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class SeatPlan(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    
    class Meta:
        unique_together = ('room', 'seat_number')
        
    def __str__(self):
        return f'{self.student} in Room {self.room.number}  Seat {self.seat_number}'
