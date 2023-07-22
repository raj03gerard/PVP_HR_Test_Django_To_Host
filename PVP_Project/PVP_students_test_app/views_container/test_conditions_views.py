from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models import Category, Test_Conditions
from ..forms import Category_form


def update_test_condition_through_form(request):
    
    if request.method=='POST':
        new_total_passing_marks= request.POST.get('total_pass_marks') 
        test_condition= Test_Conditions.objects.first()
        test_condition.total_passing_marks= new_total_passing_marks

        
        passing_marks_for_categories=[]
        for category in Category.objects.all():
            new_marks= request.POST.get(f"{category.name}_pass_marks")
            new_marks= int(new_marks) if new_marks.isdigit() else 0

            print(new_marks)

            passing_marks_for_categories.append({'category': category.name,
                                             'pass_marks': new_marks})
            category.category_passing_marks= new_marks
            category.save()


        test_condition.category_passing_marks= passing_marks_for_categories
        test_condition.save()
        print(test_condition)

    return redirect('index')

def update_test_condition():
    passing_marks_for_categories=[]
    for category in Category.objects.all():
        passing_marks_for_categories.append({'category': category.name,
                                             'pass_marks': category.category_passing_marks})
    test_condition= Test_Conditions.objects.first()
    test_condition.total_passing_marks=test_condition.total_passing_marks
    test_condition.category_passing_marks= passing_marks_for_categories
    
    test_condition.save()
