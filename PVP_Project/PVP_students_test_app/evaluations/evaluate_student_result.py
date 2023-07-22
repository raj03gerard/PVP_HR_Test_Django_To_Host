from ..models import Student, Subject, Category, Test_Conditions
from ..data_state_handle.default_data import Student_Evaluation_Results
from .evaluation_strategies import Evaluate_By_Total_Score, Evaluate_By_Marks_In_Category


class Evaluate_Results:

    def __init__(self):
        pass
    
    
    def evaluate_all_students(self):
        
        students_list= Student.objects.all()
        for student in students_list:
            has_passed= self.evaluate_student(student)
            if has_passed:
                student.evaluation_result= Student_Evaluation_Results.PASS.value
            else:
                student.evaluation_result=Student_Evaluation_Results.FAIL.value
            
            student.save()


    def evaluate_student(self,student):
        test_condition1= Evaluate_By_Total_Score.evaluate(student)
        test_condition2= Evaluate_By_Marks_In_Category.evaluate(student)
        return test_condition1 and test_condition2 
 

    
