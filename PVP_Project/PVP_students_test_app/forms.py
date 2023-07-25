from django import forms
from .models import Subject, Student, Category
import string
import random


class Category_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'category_passing_marks', ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name, eg- ARTS'}),
            'category_passing_marks': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter passing marks'}),
        }

        labels = {
            'name': 'Category Name:',
            'category_passing_marks': 'Category passing marks',
        }


class Subject_form(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'category']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject name'}),
            'category': forms.Select(attrs={'class': 'form-dropdown'}),

        }

        labels = {
            'name': 'Subject Name:',
            'category': 'Subject Category',
        }


class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'category']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'category': forms.Select(attrs={'class': 'form-dropdown'}),
        }

        labels = {
            'name': 'Enter Student Name:',
            'category': 'Student Category',
        }

    def __init__(self, *args, **kwargs):
        super(Student_form, self).__init__(*args, **kwargs)
        random_name = Student_form.generate_random_name(7)
        self.fields['name'].initial = f"Stud_{random_name}"

    def generate_random_name(length):

        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))
