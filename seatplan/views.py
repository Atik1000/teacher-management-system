from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Room, Intake, SeatPlan, Student
from .forms import SeatPlanForm, StudentForm, IntakeForm, RoomForm


from .models import Student, Intake

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'student_id', 'intake']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['intakes'] = Intake.objects.all()
        return context
    
class SeatPlanListView(ListView):
    model = SeatPlan
    template_name = 'seatplan_list.html'
    context_object_name = 'seatplans'

class SeatPlanCreateView(CreateView):
    model = SeatPlan
    form_class = SeatPlanForm
    template_name = 'seatplan_form.html'
    success_url = reverse_lazy('seatplan_list')



class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'


class IntakeListView(ListView):
    model = Intake
    template_name = 'intake_list.html'
    context_object_name = 'intakes'

class IntakeCreateView(CreateView):
    model = Intake
    form_class = IntakeForm
    template_name = 'intake_form.html'
    success_url = reverse_lazy('intake_list')

class IntakeUpdateView(UpdateView):
    model = Intake
    form_class = IntakeForm
    template_name = 'intake_form.html'
    success_url = reverse_lazy('intake_list')

class RoomListView(ListView):
    model = Room
    template_name = 'room_list.html'
    context_object_name = 'rooms'

class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'room_form.html'
    success_url = reverse_lazy('room_list')

class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'room_form.html'
    success_url = reverse_lazy('room_list')

def generate_seat_plan(request, room_number):
    room = get_object_or_404(Room, number=room_number)
    students = Student.objects.all()
    for student in students:
        try: 
            SeatPlan.objects.get(student=student)
        except SeatPlan.DoesNotExist:
            total_seat = SeatPlan.objects.filter(room=room).count()
            if room.num_seats < total_seat + 1:
                SeatPlan.objects.create(room=room, student=student, seat_number=total_seat + 1)

    context = {
        'room': room,
    }
    return render(request, 'seat_plan.html', context)
