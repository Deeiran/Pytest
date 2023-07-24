import pytest
from lib.password_checker import *
'''If password is correct return True
'''
def test_Password_validation():
    password = PasswordChecker()
    result = password.check("123!45678")
    assert result == True

'''If password is  not correct then raise an exception
'''
def test_Password_validation():
    password = PasswordChecker()
    #result = password.check("123!4")
    with pytest.raises(Exception) as e:
        password.check("123!4")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

