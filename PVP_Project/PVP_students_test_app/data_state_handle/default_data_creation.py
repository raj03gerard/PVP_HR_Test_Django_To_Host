
from ..models import  Category, Test_Conditions, Subject



def create_default_categories():
    science_category= Category(name='SCIENCE',
                           category_passing_marks=160)
    science_category.save()

    humanities_category= Category(name='HUMANITIES',
                           category_passing_marks=160)
    humanities_category.save()
    create_default_subjects()

def create_default_subjects():
    maths= Subject(name='Maths', 
                   category= Category.objects.get(name='SCIENCE'))
    maths.save()
    biology= Subject(name='Biology', 
                   category= Category.objects.get(name='SCIENCE'))
    biology.save()
    japanese= Subject(name='Japanese', 
                   category= Category.objects.get(name='HUMANITIES'))
    japanese.save()
    history= Subject(name='History', 
                   category= Category.objects.get(name='HUMANITIES'))
    history.save()
    english= Subject(name='English', 
                   category= Category.objects.get(name='HUMANITIES'))
    english.save()

    
def create_default_test_condition():
    passing_marks_for_categories=[]
    for category in Category.objects.all():
        passing_marks_for_categories.append({'category': category.name,
                                             'pass_marks': category.category_passing_marks})
    test_condition= Test_Conditions(total_passing_marks=300,
                                    category_passing_marks=passing_marks_for_categories)
    test_condition.save()



