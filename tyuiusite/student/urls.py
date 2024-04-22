from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "student"

urlpatterns = [
    path("list/", views.list, name="anketa-list"),
    path("list/<int:pk>/", views.question_list, name="question-list"),
    path("list/<int:pk>/<int:question_id>", views.answer_list, name="answer-list"),
]