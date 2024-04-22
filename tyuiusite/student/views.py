from django.shortcuts import render
from creator.models import Anketa, Questions, Answers

def list(request):
    getlist = Anketa.objects.all()
    return render(request, "student/list.html", {"getlist": getlist})

def question_list(request, pk):
    question = Questions.objects.filter(ank_id=pk)
    return render(request, "student/question_list.html", {'question': question})

def answer_list(request,pk,question_id):
    answer = Answers.objects.filter(quest_id=question_id)
    return render(request, "student/answer_list.html", {'answer': answer})