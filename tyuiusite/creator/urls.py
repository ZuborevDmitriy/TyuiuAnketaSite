from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "creator"

urlpatterns = [
    path("list/", views.list, name="anketa-list"),
    path("list/create", views.CreateAnketa.as_view(), name="anketa-create"),
    path("list/<int:pk>/update", views.UpdateAnketa.as_view(), name="anketa-update"),
    path("list/<int:pk>/delete", views.DeleteAnketa.as_view(), name="anketa-delete"),
    path("list/<int:pk>/", views.question_list, name="question-list"),
    path("list/<int:pk>/create", views.CreateQuestion.as_view(), name="question-create"),
    path("list/<int:pk>/upd", views.UpdateQuestion.as_view(), name="question-update"),
    path("list/<int:pk>/del", views.DeleteQuestion.as_view(), name="question-delete"),
]