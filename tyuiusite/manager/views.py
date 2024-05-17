from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from . models import Survey
from . forms import SurveyForm
from creator.models import Answers, Questions, Anketa
from student.models import StudentAnswer, StudentResult
from django.contrib.auth.models import User

def survey_list(request):
    current_user = request.user
    getsurvey = Survey.objects.filter(survey_author=current_user)
    return render(request, 'manager/survey_list.html', {"surveylist": getsurvey})

class CreateSurvey(CreateView):
    model = Survey
    form_class = SurveyForm
    template_name = "manager/survey_create.html"
    success_url = reverse_lazy('manager:survey-list')
    def form_valid(self, form):
        form.instance.survey_author = self.request.user.username
        return super().form_valid(form)

class UpdateSurvey(UpdateView):
    model = Survey
    form_class = SurveyForm
    template_name = "manager/survey_update.html"
    success_url = reverse_lazy('manager:survey-list')
    
class DeleteSurvey(DeleteView):
    model = Survey
    fields="__all__"
    template_name = "manager/survey_delete.html"
    success_url = reverse_lazy('manager:survey-list')
    
def test_result_view(request, pk):
    students = StudentResult.objects.filter(test_id=pk)
    students_name = StudentResult.objects.filter(test_id=pk).values_list('student_name', flat=True).distinct()
    pupils = Survey.objects.filter(pk=pk).values_list('students', flat=True).distinct()
    students_username = User.objects.filter(id__in=pupils).values_list('username', flat=True).distinct()
    if any(item in students_username for item in students_name):
        students_username=[x for x in students_username if x not in students_name]
        return render(request, "manager/test_result.html", {'students':students, 'students_username':students_username})
    else:
        return render(request, "manager/test_result.html", {'students_username':students_username})