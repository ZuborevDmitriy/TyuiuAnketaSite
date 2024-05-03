from . models import Anketa, Questions, Answers
from django.forms import ModelForm, TextInput, Select
from django import forms

class AnketaForm(ModelForm):
    class Meta:
        model = Anketa
        fields = ["anketa_title"]
        widgets = {
            "anketa_title": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Заголовок анкеты'
            })}

class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ["question"]
        widgets = {
            "question": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Вопрос'
            })}

class AnswerForm(ModelForm):
    class Meta:
        model = Answers
        fields = ["answer"]
        widgets = {
            "answer": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Заголовок анкеты'
            })}