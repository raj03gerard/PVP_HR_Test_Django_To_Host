from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models import Category
from ..forms import Category_form
from .test_conditions_views import update_test_condition
from ..data_state_handle.default_data import Default_Category_Colors
import random

# Handles creation of new categories

def create_category(request):
    template_name= 'home_page.html'
    
    if request.method=='POST':
        category_form= Category_form(request.POST)
        if(category_form.is_valid):
            
            category = category_form.save(commit=False)
           
            category.color = random.choice(list(Default_Category_Colors)).value
            category.save() 

            update_test_condition()
            return redirect('index') 
    return redirect('index')
