from . models import Anketa, Questions, Answers
from django.forms import ModelForm, TextInput

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