from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from manager.models import Survey
from . models import StudentAnswer
from creator.models import Answers, Questions, Anketa
from .forms import StudentAnswerForm
from django.utils import timezone

def list(request):
    current_user = request.user
    user_id = current_user.id
    current_time = timezone.now()
    getlist = Survey.objects.filter(students = user_id, start_time__lte=current_time, end_time__gte=current_time)
    return render(request, "student/list.html", {"getlist": getlist})

def questions_list(request, test_id):
    questions = Questions.objects.filter(ank_id=test_id)
    current_user = request.user
    user_id = current_user.id
    getlist = Survey.objects.filter(students = user_id)  
    return render(request, "student/question_list.html", {'questions':questions, "getlist": getlist})

def answer_list(request, test_id, answ_id):
    answers = Answers.objects.get(quest_id=answ_id)
    return render(request, "student/answers_list.html", {'answers':answers})

# Для ответов quest_id=answ_id

def submit_answer(request, test_id, answ_id):
    if request.method == "POST":
        student_answer_text = request.POST.get("answer_text")
        question_id = request.POST.get("question")
        answer = get_object_or_404(Answers, quest_id=answ_id)
        correct_answer = answer.answer
        if student_answer_text.upper() == correct_answer.upper():
            student_answer = StudentAnswer.objects.create(
                question_id = question_id,
                student = request.user,
                answer_text=student_answer_text,
                right_answer=True
            )
            student_answer.save()
        else:
            student_answer = StudentAnswer.objects.create(
                question_id = question_id,
                student = request.user,
                answer_text=student_answer_text,
                right_answer=False
            )
            student_answer.save()
    form = StudentAnswerForm()
    data = {
        'form':form
    }
    return render(request, 'student/submit_answer.html', data)

def result(request, test_id):
    current_user = request.user
    correct_answer_count = StudentAnswer.objects.filter(student=current_user, right_answer=True).count()
    question_count = Questions.objects.filter(ank_id=test_id).count()
    return render(request, 'student/result.html', {'correct_answer_count':correct_answer_count, 'question_count':question_count})