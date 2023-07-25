import pytest
from lib.present import *
'''return a wrap content without exception '''
def test_wrap_contents():
    present = Present()
    present.wrap(10)
    assert present.unwrap() == 10

'''return a wrap content without exception (wrap twise) '''

def test_wrap_twise():
    present = Present()
    present.wrap(50)
    with pytest.raises(Exception) as e: 
        present.wrap(40)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

'''return a unwrap content without exception '''

def test_unwrap_with_no_contents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."


