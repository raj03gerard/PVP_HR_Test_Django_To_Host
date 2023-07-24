from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models import Subject
from ..forms import Subject_form

#  Handles creation and deletion of subjects


def create_subject(request):
    template_name = 'home_page.html'

    if request.method == 'POST':
        subject_form = Subject_form(request.POST)
        if (subject_form.is_valid):
            subject_form.save()
            return redirect('index')
    return redirect('index')


def delete_subject(request, sub_id):
    print(sub_id)
    if request.method == 'POST':
        subject_to_delete = Subject.objects.get(id=sub_id)
        subject_to_delete.delete()
        return redirect('index')
    return redirect('index')
