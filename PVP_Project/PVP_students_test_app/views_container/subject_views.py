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
            new_subject = subject_form.save(commit=False)
            exisiting_subject = Subject.objects.filter(name=new_subject.name)
            if exisiting_subject.exists():
                print("Subject already exists")
                return JsonResponse({'message': f"Subject already exists"})

            else:
                new_subject.save()
                return JsonResponse({'message': 'New subject added'})
    return redirect('index')


def delete_subject(request, sub_id):
    print(sub_id)
    if request.method == 'POST':
        subject_to_delete = Subject.objects.get(id=sub_id)
        subject_to_delete.delete()
        return redirect('index')
    return redirect('index')
