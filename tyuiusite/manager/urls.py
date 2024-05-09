from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "manager"

urlpatterns = [
    path("survey-list/", views.survey_list, name="survey-list"),
    path("survey-create/", views.CreateSurvey.as_view(), name="survey-create"),
    path("survey-list/<int:pk>", views.test_result_view, name="tests-view"),
    path("survey-list/<int:pk>/update", views.UpdateSurvey.as_view(), name="tests-update"),
    path("survey-list/<int:pk>/delete", views.DeleteSurvey.as_view(), name="tests-delete"),
]