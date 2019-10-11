from python_code_4 import P1, C1, A1

def test_Professor_Class():
    course = P1.course
    classList = C1.number
    if(classList != course):
        print("\nThis professor cannot add to this class!")
    assert course == classList
    print("\nThis professor can add assignments to course!")
