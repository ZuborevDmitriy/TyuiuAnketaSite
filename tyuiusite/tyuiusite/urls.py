from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("users/", include("users.urls")),
    path("creator/", include("creator.urls")),
    path("manager/", include("manager.urls")),
    path("student/", include("student.urls")),
]
