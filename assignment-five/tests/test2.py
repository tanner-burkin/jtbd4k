from python_code_2 import TA1
import array

sections = array.array('i', [10])

def test_ta_course():

    print("\n Checking to see if TA can post to course...")
    assert sections[0] == TA1.section
