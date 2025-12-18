from django.urls import path
from . import views
from .views import student_api

urlpatterns = [
    path("", views.Home, name="home"),
    path("submit/", views.submit_form, name="submit_form"),  # ✅ fixed
    path("api/", views.student_api, name="student_api"),
]
