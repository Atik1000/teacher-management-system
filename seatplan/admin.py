from django.contrib import admin
from .models import Room, Intake, Student, SeatPlan

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'num_seats', 'num_columns')
    search_fields = ('number',)

@admin.register(Intake)
class IntakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'intake')
    search_fields = ('name', 'student_id')
    list_filter = ('intake',)

@admin.register(SeatPlan)
class SeatPlanAdmin(admin.ModelAdmin):
    list_display = ('room', 'student', 'seat_number')
    search_fields = ('room__number', 'student__name', 'student__student_id', 'seat_number')
    list_filter = ('room', 'student__intake')
