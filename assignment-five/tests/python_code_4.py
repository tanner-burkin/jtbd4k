class Course:
    def __init__(self, name, number, seats):
        self.name = name
        self.number = number
        self.seats = seats

class Professor:
    def __init__(self, name, course):
        self.name = name
        self.course = course

class Assignment:
    def __init__(self, name, dueDate):
        self.name = name
        self.dueDate = dueDate

P1 = Professor("Tim Jones", "2050")
C1 = Course("Graph Theory", "3050", 75)
A1 = Assignment("Machine Problem 1", "9/30/19")
