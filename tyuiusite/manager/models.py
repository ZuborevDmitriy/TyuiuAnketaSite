from django.db import models
from creator.models import Anketa
from django.contrib.auth import get_user_model
from django.utils import timezone

Users=get_user_model()
class Survey(models.Model):
    survey_title = models.CharField("Заголовок опроса", max_length=100)
    test = models.ManyToManyField(Anketa, verbose_name="Тесты")
    students = models.ManyToManyField(Users, verbose_name="Студенты")
    start_time = models.DateTimeField(null=True, blank=True, verbose_name="Время начала")
    end_time = models.DateTimeField(null=True, blank=True, verbose_name="Время завершения")
    def is_active(self):
        now=timezone.now()
        return self.start_time<=now<=self.end_time
    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural="Опросы"
    def __str__(self):
        return self.survey_title