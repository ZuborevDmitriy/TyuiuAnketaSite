from django.db import models

class Anketa(models.Model):
    anketa_title = models.CharField('Заголовок', max_length = 200)
    pub_date = models.DateTimeField('Дата создания', auto_now_add=True)
    def __str__(self):
        return self.anketa_title
    class Meta:
        verbose_name = "Анкета"
        verbose_name_plural="Анкеты"
        
class Questions(models.Model):
    ank = models.ForeignKey(Anketa, on_delete=models.CASCADE)
    question = models.CharField('Вопрос', max_length = 200)
    def __str__(self):
        return self.question
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural="Вопросы"

class Answers(models.Model):
    ank = models.ForeignKey(Anketa, on_delete=models.CASCADE)
    quest = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField('Ответ', max_length = 200)
    def __str__(self):
        return self.answer
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural="Ответы"