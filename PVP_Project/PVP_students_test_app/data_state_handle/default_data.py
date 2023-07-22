from enum import Enum


default_total_passing_marks=300

class Student_Evaluation_Results(Enum):
    NOT_EVALUATED= 'NOT_EVALUATED'
    PASS= 'PASS'
    FAIL= 'FAIL'


class Default_Category_Colors(Enum):
    lavender = "#E6E6FA"      
    powderBlue = "#B0E0E6"    
    almond = "#FAEBD7"    
    brown = "#CBBEB5"  
