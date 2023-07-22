from django.urls import path

from .import views
from .views_container import category_views, student_views, subject_views, test_conditions_views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_category', category_views.create_category, name='create_category'),
    path('create_subject', subject_views.create_subject, name='create_subject'),
    path('create_student', student_views.create_student, name='create_student'),
    path('update_test_condition_through_form', test_conditions_views.update_test_condition_through_form, name='update_test_condition_through_form'),
    path('get_default_colors', views.get_default_colors, name='get_default_colors'),
    
]
