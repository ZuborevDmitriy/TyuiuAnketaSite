from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "student"

urlpatterns = [
    path("list/", views.list, name="tests-list"),
    path("list/<int:test_id>", views.questions_list, name="start-test"),
    path("list/<int:test_id>/<int:answ_id>", views.submit_answer, name="get-answer"),
]