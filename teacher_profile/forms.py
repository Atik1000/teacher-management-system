from django import forms
from .models import TeacherProfile

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['department', 'full_name', 'email', 'phone_number', 'address']
