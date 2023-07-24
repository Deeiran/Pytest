from lib.check_codeword import *
'''
If it is correct codeword,
then return "Correct! Come in"
'''

def test_check_codeword_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

'''
If it is incorrect codeword,
then return "WRONG!"
'''
def test_check_codeword_incorrect():
    result = check_codeword("mouse")
    assert result == "WRONG!"
'''
If it is almost correct codeword,
then return "Close, but nope."
'''
def test_check_codeword_incorrect():
    result = check_codeword("house")
    assert result == "Close, but nope."