from django.urls import path
from .views import ExamCreateView, ExamUpdateView, ExamDetailView

urlpatterns = [
    path('exam/add/', ExamCreateView.as_view(), name='exam-add'),
    path('exam/<int:pk>/update/', ExamUpdateView.as_view(), name='exam-update'),
    path('exam/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
]
