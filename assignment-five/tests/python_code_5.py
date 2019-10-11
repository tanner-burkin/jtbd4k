class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

class Assignment:
    def __init__(self, name, description, dueDate, course):
        self.name = name
        self.description = description
        self.dueDate = dueDate
        self.course = course

S1 = Student("Steven Smith", "CS2050")
A1 = Assignment("Machine Problem 1", "Write a program.", "9/20/19", "CS3050")
