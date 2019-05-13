from django.http import HttpResponse
from django.shortcuts import render

from .models import StudentModel
from .forms import StudentForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerialize


# Create your views here.
def home(request):
    form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'simple_form/index.html', context)


@api_view(['POST'])
def student_api(request):
    serialize = StudentSerialize(data=request.POST)
    if serialize.is_valid():
        serialize.save()
        context = {
            'status': 200,
            'message': 'Inserted Successfully',
        }
    else:
        context = {
            'status': 201,
            'message': 'Validation Error',
            'errors': serialize.errors,
            'data': ''
        }
    return Response(context)


@api_view()
def student_api_list(request):
    data = StudentModel.objects.all()
    serializer = StudentSerialize(data, many=True)
    return Response(serializer.data)
