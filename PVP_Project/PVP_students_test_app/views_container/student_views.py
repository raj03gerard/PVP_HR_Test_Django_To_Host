from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models import Student, Subject
from ..forms import Student_form


# Handles creation and deletion of students

def create_student(request):
    default_subjects_list = Subject.objects.all()
    subject_list = []
    if request.method == 'POST':
        student_form = Student_form(request.POST)
        if (student_form.is_valid):
            flag = 0
            instance = student_form.save(commit=False)

            for sub in default_subjects_list:
                unverified_marks = request.POST.get(sub.name)
                verified_marks = 0
                if unverified_marks.isdigit():
                    verified_marks = int(unverified_marks)

                    if verified_marks > 100 or verified_marks < 0:
                        verified_marks = int(unverified_marks) if int(unverified_marks) >= 0 and int(
                            unverified_marks) <= 100 else max(min(int(unverified_marks), 100), 0)

                        flag = 1
                        return JsonResponse({'message': 'Invalid marks: Please enter all marks between 0 and 100'})
                    else:
                        subject_list.append({'subject': sub.name,
                                             'marks': verified_marks,
                                             'category': sub.category.name,
                                             })
                else:
                    flag = 1

            if flag == 0:
                # stud_obj = Student.objects.get(id=instance.id)
                instance.subjects = subject_list
                instance.save()
                print(f"flag= {flag}")
                return JsonResponse({'message': 'New Student created'})
            else:
                return JsonResponse({'message': 'Invalid marks: Please enter all marks between 0 and 100'})

    return JsonResponse({'message': 'Could not create new Student'})


def delete_student(request, stud_id):

    if request.method == 'POST':
        student_to_delete = Student.objects.get(id=stud_id)
        student_to_delete.delete()
        return redirect('index')
    return redirect('index')
