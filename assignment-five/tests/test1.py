from python_code_1 import P1, storedPassword

def test_correct_password():

    print("Running test example..\n")
    assert P1.query == storedPassword
