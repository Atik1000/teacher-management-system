# views.py
from django.shortcuts import render, get_object_or_404
from .models import Room, Intake, SeatPlan,Student
from .utils import assign_seat_plan

def generate_seat_plan(request, room_number):
    room = get_object_or_404(Room, number=room_number)
    students=Student.objects.all()
    for student in students:
        try: 
            SeatPlan.objects.get(student=student)
        except SeatPlan.DoesNotExist:
            total_seat=SeatPlan.objects.filter(room=room).count()

            if room.num_seats<total_seat+1:

                SeatPlan.objects.create(room=room,student=student,seat_number=total_seat+1)


    context = {
        'room': room,
        # 'seat_plans': seat_plans,
    }
    return render(request, 'seat_plan.html', context)


