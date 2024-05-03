from django.http import Http404, HttpResponse, HttpResponseRedirect
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
    fields="__all__"
    template_name = "creator/anketa_create.html"
    success_url = reverse_lazy('creator:anketa-list')

class UpdateAnketa(UpdateView):
    model = Anketa
    fields="__all__"
    template_name = "creator/anketa_update.html"
    success_url = reverse_lazy('creator:anketa-list')

class DeleteAnketa(DeleteView):
    model = Anketa
    fields="__all__"
    template_name = "creator/anketa_delete.html"
    success_url = reverse_lazy('creator:anketa-list')
    
def question_list(request, pk):
    getlist = Anketa.objects.filter(pk=pk)
    question = Questions.objects.filter(ank_id=pk)
    return render(request, "creator/question_list.html", {'questions': question, 'getlist': getlist})

class CreateQuestion(CreateView):
    model = Questions
    form_class = QuestionForm
    template_name = "creator/question_create.html"
    success_url = reverse_lazy('creator:anketa-list')
    pk_url_kwarg = 'question_id'
    def form_valid(self, form):
        form.instance.ank_id = self.kwargs['pk']
        return super().form_valid(form)

class UpdateQuestion(UpdateView):
    model = Questions
    fields="__all__"
    template_name = "creator/question_update.html"
    success_url = reverse_lazy('creator:anketa-list')
    pk_url_kwarg = 'question_id'

class DeleteQuestion(DeleteView):
    model = Questions
    fields="__all__"
    template_name = "creator/question_delete.html"
    success_url = reverse_lazy('creator:anketa-list')
    pk_url_kwarg = 'question_id'

def answer_list(request,pk,question_id):
    question = Questions.objects.filter(pk=question_id)
    answer = Answers.objects.filter(quest_id=question_id)
    return render(request, "creator/answer_list.html", {'answer': answer, 'questions': question})

class CreateAnswer(CreateView):
    model = Answers
    form_class = AnswerForm
    template_name = "creator/answer_create.html"
    success_url = reverse_lazy('creator:anketa-list')
    pk_url_kwarg = 'answer_id'
    def form_valid(self, form):
        form.instance.ank_id = self.kwargs['pk']
        form.instance.quest_id = self.kwargs['question_id']
        return super().form_valid(form)

class UpdateAnswer(UpdateView):
    model = Answers
    fields="__all__"
    template_name = "creator/answer_update.html"
    success_url = reverse_lazy('creator:anketa-list')
    pk_url_kwarg = 'answer_id'

class DeleteAnswer(DeleteView):
    model = Answers
    fields="__all__"
    template_name = "creator/answer_delete.html"
    success_url = reverse_lazy('creator:anketa-list')
    pk_url_kwarg = 'answer_id'