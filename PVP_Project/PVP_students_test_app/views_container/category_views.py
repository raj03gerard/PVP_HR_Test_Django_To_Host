from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models import Category
from ..forms import Category_form
from .test_conditions_views import update_test_condition
from ..data_state_handle.default_data import Default_Category_Colors
import random

# Handles creation of new categories


def create_category(request):
    template_name = 'home_page.html'

    if request.method == 'POST':
        category_form = Category_form(request.POST)
        if (category_form.is_valid()):

            category_data = category_form.save(commit=False)
            print(
                f"Entered category marks: {category_data.category_passing_marks}")
            category_data.color = random.choice(
                list(Default_Category_Colors)).value

            existing_category = Category.objects.filter(
                name=category_data.name.upper())

            if existing_category.exists():
                existing_category = existing_category[0]
                existing_category.category_passing_marks = category_data.category_passing_marks
                existing_category.save()
                update_test_condition()
                return JsonResponse({'message': f"Category already exists: Updated {existing_category.name}, {existing_category.category_passing_marks}"})

            else:
                category_data.save()

                update_test_condition()
                return JsonResponse({'message': 'New category created'})
    return JsonResponse({'message': 'Could not create category'})
