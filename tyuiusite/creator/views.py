from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from . models import Anketa, Questions, Answers
from . forms import AnketaForm, QuestionForm, AnswerForm

def list(request):
    getlist = Anketa.objects.all()
    return render(request, "creator/list.html", {"getlist": getlist})

class CreateAnketa(CreateView):
    model = Anketa
    form_class = AnketaForm
    template_name = "creator/anketa_create.html"
    success_url = reverse_lazy('creator:anketa-list')

class UpdateAnketa(UpdateView):
    model = Anketa
    form_class = AnketaForm
    template_name = "creator/anketa_update.html"
    success_url = reverse_lazy('creator:anketa-list')

class DeleteAnketa(DeleteView):
    model = Anketa
    template_name = "creator/anketa_delete.html"
    success_url = reverse_lazy('creator:anketa-list')
    
def question_list(request,pk):
    question = Questions.objects.filter(ank_id=pk)
    return render(request, "creator/question_list.html", {'question': question})

class CreateQuestion(CreateView):
    model = Questions
    form_class = QuestionForm
    template_name = "creator/question_create.html"
    success_url = reverse_lazy('creator:anketa-list')

class UpdateQuestion(UpdateView):
    model = Questions
    form_class = QuestionForm
    template_name = "creator/question_update.html"
    success_url = reverse_lazy('creator:anketa-list')

class DeleteQuestion(DeleteView):
    model = Questions
    template_name = "creator/question_delete.html"
    success_url = reverse_lazy('creator:anketa-list')

def answer_list():
    answer = Answers.objects.filter(quest_id=question_id)
    return render(request, "creator/answer_list.html", {'answer': answer})

class CreateAnswer(CreateView):
    model = Answers
    form_class = AnswerForm
    template_name = "creator/answer_create.html"
    success_url = reverse_lazy('creator:anketa-list')

class UpdateAnswer(UpdateView):
    model = Answers
    form_class = AnswerForm
    template_name = "creator/answer_update.html"
    success_url = reverse_lazy('creator:anketa-list')

class DeleteAnswer(DeleteView):
    model = Answers
    template_name = "creator/answer_delete.html"
    success_url = reverse_lazy('creator:anketa-list')