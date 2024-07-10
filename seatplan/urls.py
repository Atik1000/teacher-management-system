# from django.urls import path
# from .views import (
#     RoomListView, RoomDetailView, RoomCreateView, RoomUpdateView, RoomDeleteView,
#     IntakeListView, IntakeDetailView, IntakeCreateView, IntakeUpdateView, IntakeDeleteView
# )

# urlpatterns = [
#     # Room URLs
#     path('rooms/', RoomListView.as_view(), name='room-list'),
#     path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
#     path('rooms/create/', RoomCreateView.as_view(), name='room-create'),
#     path('rooms/<int:pk>/update/', RoomUpdateView.as_view(), name='room-update'),
#     path('rooms/<int:pk>/delete/', RoomDeleteView.as_view(), name='room-delete'),

#     # Intake URLs
#     path('intakes/', IntakeListView.as_view(), name='intake-list'),
#     path('intakes/<int:pk>/', IntakeDetailView.as_view(), name='intake-detail'),
#     path('intakes/create/', IntakeCreateView.as_view(), name='intake-create'),
#     path('intakes/<int:pk>/update/', IntakeUpdateView.as_view(), name='intake-update'),
#     path('intakes/<int:pk>/delete/', IntakeDeleteView.as_view(), name='intake-delete'),
# ]
