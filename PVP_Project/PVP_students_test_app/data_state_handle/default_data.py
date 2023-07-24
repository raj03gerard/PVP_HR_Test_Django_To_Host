from enum import Enum

# contains some default data like enums for Student_Evaluation_Results,
# colors for the different categories( Default_Category_Colors) , etc


default_total_passing_marks = 300


class Student_Evaluation_Results(Enum):
    NOT_EVALUATED = 'NOT_EVALUATED'
    PASS = 'PASS'
    FAIL = 'FAIL'


class Default_Category_Colors(Enum):
    lavender = "#E6E6FA"
    powderBlue = "#B0E0E6"
    almond = "#FAEBD7"
    brown = "#CBBEB5"
    green = "#F2EE9D"
    lightBlue = "#78C1F3"
    orange = "#FFA41B"
    pink = "#F1D4E5"
    pinkOrange = "#F99B7D"
