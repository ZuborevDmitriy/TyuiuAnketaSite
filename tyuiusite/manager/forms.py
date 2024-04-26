from . models import Survey
from django.forms import ModelForm, TextInput, Select, DateInput, TimeInput, DateTimeInput, SelectMultiple

class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ["survey_title","test","students","start_time","end_time"]
        widgets = {
            "survey_title": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Заголовок опроса'
            }),
            "test": Select(attrs={
                'class':'form-control',
                'type':"choise"
            }),
            "students": SelectMultiple(attrs={
                'class':'form-select'
            }),
            "start_time": DateTimeInput(attrs={
                'class':'form-control',
                'type':"datetime-local"
                
            }),
            "end_time": DateTimeInput(attrs={
                'class':'form-control',
                'type':"datetime-local"
            })}