from django.forms import ModelForm, TextInput, Select, DateInput, TimeInput, DateTimeInput, SelectMultiple
from .models import StudentAnswer

class StudentAnswerForm(ModelForm):
    class Meta:
        model = StudentAnswer
        fields = ['question','answer_text']
        widgets = {
            "answer_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ответ'
            })
        }