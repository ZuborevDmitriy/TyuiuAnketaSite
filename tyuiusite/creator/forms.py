from . models import Anketa, Questions, Answers
from django.forms import ModelForm, TextInput

class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ["question"]

class AnswerForm(ModelForm):
    class Meta:
        model = Answers
        fields = ["answer"]