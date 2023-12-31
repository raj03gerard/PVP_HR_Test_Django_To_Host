
from ..models import Category, Test_Conditions, Subject
from .default_data import Default_Category_Colors
import random


# contains functions to create the default data for the app

def create_default_categories():
    default_category = Category(name='NONE',
                                category_passing_marks=0,
                                color=random.choice(list(Default_Category_Colors)).value)

    default_category.save()

    science_category = Category(name='SCIENCE',
                                category_passing_marks=160,
                                color=random.choice(list(Default_Category_Colors)).value)

    science_category.save()
    print(science_category)
    humanities_category = Category(name='HUMANITIES',
                                   category_passing_marks=160,
                                   color=random.choice(list(Default_Category_Colors)).value)
    humanities_category.save()
    print(humanities_category)



def create_default_subjects():
    english = Subject(name='English',
                      category=Category.objects.get(name='NONE'))
    english.save()
    maths = Subject(name='Maths',
                    category=Category.objects.get(name='SCIENCE'))
    maths.save()

    science = Subject(name='Science',
                      category=Category.objects.get(name='SCIENCE'))
    science.save()
    japanese = Subject(name='Japanese',
                       category=Category.objects.get(name='HUMANITIES'))
    japanese.save()
    history = Subject(name='History',
                      category=Category.objects.get(name='HUMANITIES'))
    history.save()


def create_default_test_condition():
    passing_marks_for_categories = []
    for category in Category.objects.all():
        passing_marks_for_categories.append({'category': category.name,
                                             'pass_marks': category.category_passing_marks})
    test_condition = Test_Conditions(total_passing_marks=300,
                                     category_passing_marks=passing_marks_for_categories)
    test_condition.save()
