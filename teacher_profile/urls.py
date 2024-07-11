from django.urls import path
from .views import DepartmentListView, DepartmentDetailView, TeacherListView, TeacherProfileCreateView, TeacherProfileDetailView,TeacherProfileUpdateView

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/create/', TeacherProfileCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/', TeacherProfileDetailView.as_view(), name='teacher_profile_detail'),

    path('teachers/<int:pk>/', TeacherProfileUpdateView.as_view(), name='teacher_profile_update'),
]
