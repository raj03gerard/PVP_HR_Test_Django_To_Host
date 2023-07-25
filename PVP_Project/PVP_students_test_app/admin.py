from django.contrib import admin
from .models import Student, Subject, Category, Test_Conditions, Default_Project_Data

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Test_Conditions)
admin.site.register(Default_Project_Data)
# Register your models here.
