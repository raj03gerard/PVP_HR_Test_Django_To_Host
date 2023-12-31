from itertools import combinations
from abc import ABC, abstractmethod
from ..models import Student, Subject, Category, Test_Conditions

# This is an abstract class that contains definition for the evaluate
# method. New evaluation strategies are created from this class


class Evaluation_Strategy(ABC):

    @abstractmethod
    def evaluate(student):
        pass

# This class inherits the Evaluation_Strategy class, to evaluate
# the student result based on total_score


class Evaluate_By_Total_Score(Evaluation_Strategy):
    def __init__(self):
        pass

    def evaluate(self, student):

        try:
            total_passing_marks = Test_Conditions.objects.first().total_passing_marks

        except:
            total_passing_marks = 300
        total_marks = 0
        for subject_data in student.subjects:
            total_marks += int(subject_data['marks'])

        if total_marks >= total_passing_marks:
            return True
        else:
            return False

#  This class also inherits the Evaluation_Strategy class, to evaluate
#  the student result marks in his category


class Evaluate_By_Marks_In_Category(Evaluation_Strategy):
    def __init__(self):
        pass

    def evaluate(self, student):
        category_pass_marks = 0
        try:
            test_condition = Test_Conditions.objects.first()

            for pass_mark in test_condition.category_passing_marks:
                if pass_mark['category'] == student.category.name:
                    category_pass_marks = pass_mark['pass_marks']
        except:
            category_pass_marks = 100

        marks_list = []
        for subject_data in student.subjects:
            if subject_data['category'] == student.category.name:
                marks_list.append(int(subject_data['marks']))

        is_passing_by_category = Evaluate_By_Marks_In_Category.are_marks_above_passing_marks(
            marks_list, category_pass_marks)
        return is_passing_by_category

    def are_marks_above_passing_marks(marks_list,  passing_marks):
        marks_sum = sum(marks_list)
        if marks_sum >= passing_marks:
            return True
        else:
            return False
