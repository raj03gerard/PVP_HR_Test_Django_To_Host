from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Student, Subject, Category, Student_Evaluation_Results, Test_Conditions, Default_Project_Data
from .forms import Subject_form, Student_form, Category_form
from .evaluations.evaluate_student_result import Evaluate_Results
from .data_state_handle.default_data_creation import create_default_test_condition, create_default_categories
from .data_state_handle.default_data import Default_Category_Colors

# The starting point for the execution of the app, that handles
# the route to the home page(index()).


def index(request):

    default_data_check()

    template_name = 'home_page.html'
    category_form = Category_form()
    subject_form = Subject_form()
    student_form = Student_form()
    students = Student.objects.all()
    subjects = Subject.objects.all()
    categories = Category.objects.all()
    test_condition = Test_Conditions.objects.first()

    no_of_students_passed = Evaluate_Results().evaluate_all_students()
    context = {'students': students,
               'categories': categories,
               'subjects': subjects,
               'category_form': category_form,
               'subject_form': subject_form,
               'student_form': student_form,
               'test_condition': test_condition,
               'no_of_students': students.count(),
               'no_of_students_passed': no_of_students_passed,
               }

    return render(request, template_name, context)


# The default_data_check() function checks whether the app
# has some default data in it as soon as the home page loads

def default_data_check():

    if Default_Project_Data.objects.all().count() <= 0:
        default_project_data = Default_Project_Data(max_student_id=0)
        default_project_data.save()

    if Category.objects.all().count() > 0:
        if (Test_Conditions.objects.all().count() <= 0):
            create_default_test_condition()

    else:
        create_default_categories()
        create_default_test_condition()


# The get_default_colors() function gets the default color schemes for the app

def get_default_colors(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        category_colors = {}
        for category in categories:
            category_colors[category.name] = f"{category.color}"
        colors_list = {}
        for color in Default_Category_Colors:
            colors_list[color.name] = color.value
        print(colors_list)
        return JsonResponse({'colors_list': colors_list,
                             'categories': category_colors})
    return JsonResponse({'colors_list': []})
