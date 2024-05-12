from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from . models import Survey
from . forms import SurveyForm
from creator.models import Answers, Questions, Anketa
from student.models import StudentAnswer, StudentResult
from django.contrib.auth.models import User

def survey_list(request):
    getsurvey = Survey.objects.all()
    return render(request, 'manager/survey_list.html', {"surveylist": getsurvey})

class CreateSurvey(CreateView):
    model = Survey
    form_class = SurveyForm
    template_name = "manager/survey_create.html"
    success_url = reverse_lazy('manager:survey-list')

class UpdateSurvey(UpdateView):
    model = Survey
    form_class = SurveyForm
    template_name = "manager/survey_update.html"
    success_url = reverse_lazy('manager:survey-update')
    
class DeleteSurvey(DeleteView):
    model = Survey
    fields="__all__"
    template_name = "manager/survey_delete.html"
    success_url = reverse_lazy('manager:survey-delete')
    
def test_result_view(request, pk):
    students = StudentResult.objects.filter(test_id=pk)
    students_username=[]
    if not students.exists():
        pupils = Survey.objects.filter(pk=pk).values_list('students', flat=True).distinct()
        students_username = User.objects.filter(id__in=pupils)
    return render(request, "manager/test_result.html", {'students':students, 'student_username':students_username})