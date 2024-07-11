from django import forms
from .models import SeatPlan, Student, Intake, Room
from .widgets import BootstrapFormControl

class SeatPlanForm(forms.ModelForm):
    class Meta:
        model = SeatPlan
        fields = ['room', 'student', 'seat_number']
        widgets = {
            'room': BootstrapFormControl(),
            'student': BootstrapFormControl(),
            'seat_number': BootstrapFormControl(),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'intake']
        widgets = {
            'name': BootstrapFormControl(),
            'student_id': BootstrapFormControl(),
            'intake': BootstrapFormControl(),
        }

class IntakeForm(forms.ModelForm):
    class Meta:
        model = Intake
        fields = ['name']
        widgets = {
            'name': BootstrapFormControl(),
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'num_seats', 'num_columns']
        widgets = {
            'number': BootstrapFormControl(),
            'num_seats': BootstrapFormControl(),
            'num_columns': BootstrapFormControl(),
        }
