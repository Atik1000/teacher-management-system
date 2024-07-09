from django.urls import path
from .views import RoomCreateView, RoomDetailView

urlpatterns = [
    path('room/add/', RoomCreateView.as_view(), name='room-add'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
]
