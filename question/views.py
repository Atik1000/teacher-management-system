from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView,View
from .models import Exam
from .forms import ExamForm
from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


class ExamCreateView(View):
    model = Exam
    form_class = ExamForm
    template_name = 'exam_form.html'

    def get(self, request,*args,**kwargs):
        form=self.form_class()
        context={
            'form':form
        }
        return render(request,self.template_name,context)
    
    def post(self, request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            obj=form.save()
            return redirect('exam-detail',obj.pk)
        context={
            'form':form
        }
        return render(request,self.template_name,context)
    

class ExamUpdateView(UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'exam_form.html'

    def get_success_url(self):
        return redirect('exam-detail', self.object.pk)

class ExamDetailView(DetailView):
    model = Exam
    template_name = 'exam_detail.html'
    context_object_name = 'exam'


def generate_pdf(request, exam_id):
    # Fetch exam details based on exam_id
    exam = get_object_or_404(Exam, id=exam_id)
    
    # Render the template with exam details
    html_string = render_to_string('exam_detail.html', {'exam': exam})
    
    # Create an HTML object with WeasyPrint
    html = HTML(string=html_string)
    
    # Generate the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=exam_{exam_id}.pdf'
    html.write_pdf(response)
    
    return response
