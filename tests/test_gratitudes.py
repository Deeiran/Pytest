from lib.gratitudes import *
''' return the whole gratitude sentence'''
def test_gratitude_full_sentence():
    gratitude = Gratitudes()
    gratitude.add("what you have!")
    gratitude.add("let me know")
    gratitude.add("Thank you")
    result = gratitude.format()
    assert result == "Be grateful for: what you have!, let me know, Thank you"

