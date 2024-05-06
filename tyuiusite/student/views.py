from django.http import HttpResponse
from django.shortcuts import redirect, render
from manager.models import Survey
from . models import StudentAnswer
from creator.models import Answers, Questions, Anketa
from .forms import StudentAnswerForm

def list(request):
    current_user = request.user
    user_id = current_user.id
    getlist = Survey.objects.filter(students = user_id)  
    return render(request, "student/list.html", {"getlist": getlist})

def questions_list(request, test_id):
    questions = Questions.objects.filter(ank_id=test_id)
    return render(request, "student/question_list.html", {'questions':questions})

def answer_list(request, test_id, answ_id):
    answers = Answers.objects.get(quest_id=answ_id)
    return render(request, "student/answers_list.html", {'answers':answers})

# Для ответов quest_id=answ_id

def submit_answer(request, test_id, answ_id):
    if request.method == "POST":
        student_answer = StudentAnswerForm(request.POST.get('answer_text'))
        answer = Answers.objects.get(quest_id=answ_id)
        correct_answer = answer.answer
        if student_answer == correct_answer:
            return HttpResponse("Верно")
        else:
            return HttpResponse("Неверно")
    else:
        form = StudentAnswerForm()
        data = {
            'form':form
        }
        return render(request, 'student/submit_answer.html', data)