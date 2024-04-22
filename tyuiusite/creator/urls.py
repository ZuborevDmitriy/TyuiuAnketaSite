from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "creator"

urlpatterns = [
    path("list/", views.list, name="list"),
    path("list/create", views.CreateAnketa.as_view(), name="list-create"),
    path("list/<int:pk>/update", views.UpdateAnketa.as_view(), name="list-update"),
    path("list/<int:pk>/delete", views.DeleteAnketa.as_view(), name="list-delete"),
    path("list/<int:pk>/", views.question_list, name="question-list"),
    path("list/<int:pk>/create", views.CreateQuestion.as_view(), name="question-create"),
    path("list/<int:pk>/<question_id>/update", views.UpdateQuestion.as_view(), name="question-update"),
    path("list/<int:pk>/<question_id>/delete", views.DeleteQuestion.as_view(), name="question-delete"),
    path("list/<int:pk>/<question_id>/", views.answer_list, name="answer-list"),
    path("list/<int:pk>/<question_id>/create", views.CreateAnswer.as_view(), name="answer-create"),
]