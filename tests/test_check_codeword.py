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
'''
If the last letter is wrong,
then return "WRONG!"
'''
def test_check_codeword_last_letter_incorrect():
    result = check_codeword("hotel")
    assert result == "WRONG!"

'''
If the first letter is wrong,
then return "WRONG!"
'''
def test_check_codeword_first_letter_incorrect():
    result = check_codeword("love")
    assert result == "WRONG!"