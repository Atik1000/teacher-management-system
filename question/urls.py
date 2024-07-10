from django.urls import path
from .views import ExamCreateView, ExamUpdateView, ExamDetailView,generate_pdf

urlpatterns = [
    path('exam/add/', ExamCreateView.as_view(), name='exam-add'),
    path('exam/<int:pk>/update/', ExamUpdateView.as_view(), name='exam-update'),
    path('exam/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    path('generate-pdf/<int:exam_id>/', generate_pdf, name='generate_pdf'),

]
