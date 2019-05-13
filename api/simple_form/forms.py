from django import forms

from .models import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control name'}),
            'roll': forms.TextInput(attrs={'class': 'form-control roll'})
        }
