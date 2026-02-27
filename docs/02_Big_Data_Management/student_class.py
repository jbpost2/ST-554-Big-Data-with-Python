class student:
    course = '554'
    department = 'st'
    grades = None
    
    def __init__(self, name: str, unity: str):
        self.full_name = name
        self.unity_id = unity
    
    def __str__(self):
        if self.grades is None:
            return f"Student(name={self.full_name}, unity_id={self.unity_id})"
        else:
            return f"Student(name={self.full_name}, unity_id={self.unity_id}, grades={self.grades})"
      
    @property
    def split_name(self) -> tuple[str, str]:
        """Return the first name and last name"""
        first, last = self.full_name.split(" ")
        return first, last
    
    @classmethod
    def with_grades(self, name: str, unity: str, grades: list):
        student = self(name, unity)
        student.grades = grades
        return student
      
    def add_grade(self, grade: list):
        student = self
        if student.grades is None:
            student.grades = grade
        else:
            student = student.grades.extend(grade)
        return student

#create an instance
x = student("Justin Post", "jbpost2")

#check out the attributes
print(x.course)
print(x.full_name)
print(x.unity_id)
print(x.split_name)

#create an instance with grades
x = student.with_grades("Justin Post", "jbpost2", [3, 10, 40])
print(x.grades)

#add grades
x.add_grade([12, 11])
print(x.grades)

#check our print functionality
print(x)
