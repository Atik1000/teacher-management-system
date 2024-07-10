# utils.py
from .models import SeatPlan, Student

def assign_seat_plan(room, intakes):
    seats_per_column = room.num_seats // room.num_columns
    seat_plans = []
    seat_number = 1  # Start seat numbering from 1

    for intake in intakes:
        students = Student.objects.filter(intake=intake).order_by('student_id')
        
        for student in students:
            if seat_number > room.num_seats:
                break  # Stop if we exceed the number of available seats

            column = (seat_number - 1) // seats_per_column + 1
            seat_in_column = (seat_number - 1) % seats_per_column + 1
            
            seat_plans.append(SeatPlan(room=room, student=student, column=column, seat_number=seat_number))
            seat_number += 1

    SeatPlan.objects.bulk_create(seat_plans)
