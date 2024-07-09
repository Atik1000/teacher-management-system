from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Exam
from .forms import ExamForm

class ExamCreateView(CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'exam_form.html'

    def get_success_url(self):
        return reverse('exam-detail', kwargs={'pk': self.object.pk})

class ExamUpdateView(UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'exam_form.html'

    def get_success_url(self):
        return reverse('exam-detail', kwargs={'pk': self.object.pk})

class ExamDetailView(DetailView):
    model = Exam
    template_name = 'exam_detail.html'
    context_object_name = 'exam'
