from lib.string_Builder import *
'''return the lenth of the string'''
def test_return_of_the_lenth():
    word = StringBuilder()
    word.add("Makers")
    result = word.size()
    assert result == 6

'''return the wholestring'''
def test_return_of_the_string():
    word = StringBuilder()
    word.add("Makers")
    result = word.output()
    assert result == "Makers"