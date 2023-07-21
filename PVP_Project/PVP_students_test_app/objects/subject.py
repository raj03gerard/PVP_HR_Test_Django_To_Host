class Subject(object):
    def __init__(self, title, max_marks, subject_type):
        
        self.title= title
        self.max_marks= max_marks
        self.subject_type= subject_type

    def getMaxMarks(self):
        return self.max_marks