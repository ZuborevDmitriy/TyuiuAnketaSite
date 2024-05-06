from django.db import models
from creator.models import Questions

class StudentAnswer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.CharField('Ответ', max_length = 200)
    date_answered = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.answer_text
    class Meta:
        verbose_name = "Ответ студента"
        verbose_name_plural = "Ответы студента"