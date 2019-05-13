from django.shortcuts import render
from rest_framework import  viewsets
# Create your views here.
from .models import Student
from .serializers import StudentSerializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers