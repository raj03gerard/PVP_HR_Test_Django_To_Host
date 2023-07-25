from django.contrib import admin
from .models import Student, Subject, Category, Test_Conditions

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Test_Conditions)

# Register your models here.
