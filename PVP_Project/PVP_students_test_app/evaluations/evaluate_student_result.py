from ..models import Student, Subject, Category, Test_Conditions
from ..data_state_handle.default_data import Student_Evaluation_Results
from .evaluation_strategies import Evaluation_Strategy, Evaluate_By_Total_Score, Evaluate_By_Marks_In_Category

# This class handles evaluation of each student’s result.


class Evaluate_Results:

    def __init__(self, evaluation_strategies):
        self.evaluation_strategies = evaluation_strategies

    def evaluate_all_students(self):

        students_list = Student.objects.all()
        no_of_students_passed = 0
        for student in students_list:
            has_passed = self.evaluate_student(student)
            if has_passed:
                student.evaluation_result = Student_Evaluation_Results.PASS.value
                no_of_students_passed += 1
            else:
                student.evaluation_result = Student_Evaluation_Results.FAIL.value

            student.save()

        return no_of_students_passed

    def evaluate_student(self, student):
        # test_condition1 = Evaluate_By_Total_Score.evaluate(student)
        # test_condition2 = Evaluate_By_Marks_In_Category.evaluate(student)
        has_passed = True
        for strategy in self.evaluation_strategies:
            has_passed = has_passed and strategy.evaluate(student)

        # return test_condition1 and test_condition2
        return has_passed
