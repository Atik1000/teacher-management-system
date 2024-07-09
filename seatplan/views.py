from django.urls import reverse
from django.views.generic import CreateView, DetailView
from .models import Room, Column, Student
from .forms import RoomForm

class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'room_form.html'

    def get_success_url(self):
        return reverse('room-detail', kwargs={'pk': self.object.pk})

class RoomDetailView(DetailView):
    model = Room
    template_name = 'room_detail.html'
    context_object_name = 'room'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = Column.objects.filter(room=self.object)
        context['intake1'] = Column.objects.filter(room=self.object, intake__name='Intake 1')
        context['intake2'] = Column.objects.filter(room=self.object, intake__name='Intake 2')
        return context
