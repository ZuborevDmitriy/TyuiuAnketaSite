from django.shortcuts import redirect, render
from manager.models import Survey
from . forms import AnswerForm
from creator.models import Answers, Questions, Anketa

def list(request):
    current_user = request.user
    user_id = current_user.id
    getlist = Survey.objects.filter(students = user_id)  
    return render(request, "student/list.html", {"getlist": getlist})

def questions_list(request, test_id):
    questions = Questions.objects.filter(ank_id = test_id)
    return render(request, "student/start_test.html", {'questions':questions})

def answer_list(request, test_id, answer_id):
    answers = Answers.objects.filter(quest_id = test_id)
    return render(request, "student/answer_list.html", {'answer':answers})

# def submit_answers(request, answer_id):