from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Department, TeacherProfile
from .forms import TeacherProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Department, TeacherProfile
from .forms import TeacherProfileForm

class TeacherProfileCreateView(CreateView):
    model = TeacherProfile
    form_class = TeacherProfileForm
    template_name = 'teacherprofile_form.html'
    success_url = reverse_lazy('teacher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context

class TeacherProfileUpdateView(UpdateView):
    model = TeacherProfile
    form_class = TeacherProfileForm
    template_name = 'teacherprofile_form.html'
    success_url = reverse_lazy('teacher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context
class TeacherListView(ListView):
    model = TeacherProfile
    template_name = 'teacher_list.html'
    context_object_name = 'teachers'

class TeacherProfileDetailView(DetailView):
    model = TeacherProfile
    template_name = 'teacher_profile_detail.html'
    context_object_name = 'teacher'


class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department_detail.html'
    context_object_name = 'department'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = TeacherProfile.objects.filter(department=self.object)
        return context

