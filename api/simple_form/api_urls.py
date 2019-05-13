from django.urls import path
from . import views

urlpatterns = [
    path('student_api', views.student_api, name="student_api"),
    path('list', views.student_api_list, name="list")
]
