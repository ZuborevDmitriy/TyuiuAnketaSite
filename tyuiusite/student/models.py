from django.db import models
from django.dispatch import receiver
from creator.models import Questions, Answers, Anketa
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class StudentAnswer(models.Model):
    test = models.ForeignKey(Anketa, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.CharField('Ответ', max_length = 200, null=True)
    date_answered = models.DateTimeField(auto_now=True)
    right_answer = models.BooleanField(default=False)
    def __str__(self):
        return self.answer_text
    class Meta:
        verbose_name = "Ответ студента"
        verbose_name_plural = "Ответы студента"
        
class StudentResult(models.Model):
    test = models.ForeignKey(Anketa, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.IntegerField()
    def __str__(self):
        return self.student
    class Meta:
        verbose_name = "Результат теста"
        verbose_name_plural = "Результаты тестов"