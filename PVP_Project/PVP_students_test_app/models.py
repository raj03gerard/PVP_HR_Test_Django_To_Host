from django.db import models
from .data_state_handle.default_data import Student_Evaluation_Results
from .data_state_handle.default_data import Default_Category_Colors
import random

# This file contains the classes for Student, Subject, Category and Test_Conditions.
# All of these classes inherit from the Django models.Model class, which allows them
# to be created as individual tables in the database,


class Category(models.Model):
    name = models.CharField(max_length=200)
    category_passing_marks = models.IntegerField(default=100)
    color = models.CharField(max_length=10, choices=[(
        color.value, color.name) for color in Default_Category_Colors])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Category, self).save(*args, **kwargs)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} {self.id} "


class Student(models.Model):
    name = models.CharField(max_length=200)
    subjects = models.JSONField(null=True, default=list)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    evaluation_result = models.CharField(max_length=100,
                                         choices=[(result_type.value, result_type.name)
                                                  for result_type in Student_Evaluation_Results],
                                         default=Student_Evaluation_Results.NOT_EVALUATED.value)

    def __str__(self):
        return self.name


class Test_Conditions(models.Model):
    total_passing_marks = models.IntegerField(default=300)
    category_passing_marks = models.JSONField(null=True, default=list)

    def __str__(self):
        return f"total_passing_marks: {self.total_passing_marks}"
