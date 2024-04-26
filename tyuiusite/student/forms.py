from creator.models import Answers
from django.forms import ModelForm, TextInput, Select, DateInput, TimeInput, DateTimeInput, SelectMultiple

class AnswerForm(ModelForm):
      class Meta:
        model = Answers
        fields = ["answer"]
        widgets = {
            "answer": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Заголовок анкеты'
            })}