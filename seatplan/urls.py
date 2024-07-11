from django.urls import path
from .views import (
    RoomListView, RoomCreateView, RoomUpdateView, 
    IntakeListView, IntakeCreateView, IntakeUpdateView, 
     StudentCreateView,
    SeatPlanListView, SeatPlanCreateView, StudentListView
)

urlpatterns = [
    # Room URLs
    path('room/', RoomListView.as_view(), name='room_list'),
    path('room/create/', RoomCreateView.as_view(), name='room_create'),
    path('room/<int:pk>/update/', RoomUpdateView.as_view(), name='room_update'),

    # Intake URLs
    path('intake/', IntakeListView.as_view(), name='intake_list'),
    path('intake/create/', IntakeCreateView.as_view(), name='intake_create'),
    path('intake/<int:pk>/update/', IntakeUpdateView.as_view(), name='intake_update'),

    # Student URLs

    path('student/', StudentListView.as_view(), name='student_list'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),

    # SeatPlan URLs
    path('seatplan/', SeatPlanListView.as_view(), name='seatplan_list'),
    path('seatplan/create/', SeatPlanCreateView.as_view(), name='seatplan_create'),
]
