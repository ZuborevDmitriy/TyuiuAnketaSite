from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from manager.models import Survey
from . models import StudentAnswer, StudentResult
from creator.models import Answers, Questions, Anketa
from .forms import StudentAnswerForm
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse, reverse_lazy

def list(request):
    current_user = request.user
    user_id = current_user.id
    current_time = timezone.now()
    getlist = Survey.objects.filter(students = user_id, start_time__lte=current_time, end_time__gte=current_time)
    return render(request, "student/list.html", {"getlist": getlist})

def questions_list(request, test_id):
    survey = Survey.objects.get(pk=test_id)
    survey_id = Survey.objects.filter(pk=test_id).values_list('test_id', flat=True)
    questions = Questions.objects.filter(ank_id__in=survey_id)
    return render(request, "student/question_list.html", {'survey':survey, 'questions':questions})

def answer_list(request, test_id, answ_id):
    answers = Answers.objects.get(quest_id=answ_id)
    return render(request, "student/answers_list.html", {'answers':answers})

def type_of_answers(answer):
    if isinstance(answer, str):
        return answer.strip().lower()
    return str(answer).strip().lower()

def submit_answer(request, test_id, answ_id):
    answer_count = StudentAnswer.objects.filter(student=request.user, question_id=answ_id).exists()
    survey_id = Survey.objects.filter(pk=test_id).values_list('test_id', flat=True)
    if answer_count:
        return redirect('student:tests-list')
    if request.method == "POST":
        student_answer_text = request.POST.get("answer_text")
        answer = get_object_or_404(Answers, quest_id=answ_id)
        correct_answer = answer.answer
        student_answer_text_low = type_of_answers(student_answer_text)
        correct_answer_low = type_of_answers(correct_answer)
        print(student_answer_text_low)
        print(correct_answer_low)
        dynamic_url = f'http://127.0.0.1:8000/student/list/{test_id}'
        if student_answer_text_low == correct_answer_low:
            student_answer = StudentAnswer.objects.create(
                test_id = survey_id,
                question_id = answ_id,
                student = request.user,
                answer_text=student_answer_text,
                right_answer=True
            )
            student_answer.save()
        else:
            student_answer = StudentAnswer.objects.create(
                test_id = survey_id,
                question_id = answ_id,
                student = request.user,
                answer_text=student_answer_text,
                right_answer=False
            )
            student_answer.save()
        return redirect(dynamic_url)
    form = StudentAnswerForm()
    data = {
        'form':form
    }
    return render(request, 'student/submit_answer.html', data)

def result(request, test_id):
    current_user = request.user
    user_id = current_user.id
    survey = Survey.objects.get(pk=test_id)
    survey_id = Survey.objects.filter(pk=test_id).values_list('test_id', flat=True)
    correct_answer_count = StudentAnswer.objects.filter(student_id=user_id, test_id__in=survey_id, right_answer=True).count()
    question_count = Questions.objects.filter(ank_id__in=survey_id).count()
    percent = int((correct_answer_count/question_count)*100)
    return render(request, 'student/result.html', {'correct_answer_count':correct_answer_count, 'question_count':question_count,
                                                   'percent':percent, 'survey':survey})

def send_result(request, test_id):
    current_user = request.user
    user_id = current_user.id
    survey = Survey.objects.get(pk=test_id)
    survey_id = survey.test_id
    results_count = StudentResult.objects.filter(student=request.user, test=test_id).exists()
    if results_count:
        return redirect('student:tests-list')
    correct_answer_count = StudentAnswer.objects.filter(student=user_id, test = survey_id, right_answer=True).count()
    print(correct_answer_count)
    question_count = Questions.objects.filter(ank_id=test_id).count()
    if correct_answer_count == 0:
        student_result = StudentResult.objects.create(
            test_id = test_id,
            student = current_user,
            student_name = current_user.username,
            result = 0
        )
    else:
        percent = int((correct_answer_count/question_count)*100)
        student_result = StudentResult.objects.create(
            test_id = test_id,
            student = current_user,
            student_name = current_user.username,
            result = percent
        )
    student_result.save()
    return redirect('student:tests-list')