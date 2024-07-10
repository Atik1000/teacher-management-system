from django.db import models
from django.conf import settings

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.dept_name

class TeacherProfile(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return f'{self.full_name} {self.department}'
