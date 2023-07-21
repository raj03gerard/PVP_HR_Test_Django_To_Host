from itertools import combinations
from abc import ABC, abstractmethod
from ..models import Student, Subject, Category, Test_Conditions

class Evaluation_Strategy(ABC):
    @abstractmethod
    def evaluate( student):
        pass

class Evaluate_By_Total_Score(Evaluation_Strategy):
    def evaluate( student):
        try:
            total_passing_marks= Test_Conditions.objects.first().total_passing_marks
            
        except:
            total_passing_marks= 300
        total_marks= 0
        for subject_data in student.subjects:
            total_marks+= int( subject_data['marks'])
        
        if total_marks>= total_passing_marks:
            return True
        else:
            return False
        
class Evaluate_By_Marks_In_Category(Evaluation_Strategy):
    def evaluate( student):
        category_pass_marks= 0
        try:
            test_condition= Test_Conditions.objects.first()

            for pass_mark in test_condition.category_passing_marks:
                if pass_mark['category']== student.category.name:
                    category_pass_marks= pass_mark['pass_marks']
        except:
            category_pass_marks=100

        marks_list= []
        for subject_data in student.subjects:
            if subject_data['category']==student.category.name:
                marks_list.append( int( subject_data['marks']))

        is_passing_by_category= Evaluate_By_Marks_In_Category.are_marks_above_passing_marks(marks_list, 2, category_pass_marks)
        return is_passing_by_category
    
    def are_marks_above_passing_marks( marks_list, no_of_subjects, passing_marks):
        for comb in combinations(marks_list, no_of_subjects):
            if (sum(comb) > passing_marks):
                return True
        return False
