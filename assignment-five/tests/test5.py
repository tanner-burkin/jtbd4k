from python_code_5 import A1, S1

def test_Student_ASsignment_Availability():
    assignmentClass = A1.course
    studentClass = S1.course
    assert assignmentClass == studentClass
    
