from lib.counter import *
'''Return the counted nmbers'''
def test_the_user_counted_number():
    count = Counter()
    count.add(100)
    result = count.report()
    assert result == "Counted to 100 so far."

    