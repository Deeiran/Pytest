import pytest
from lib.present import *
'''return a wrap content'''
def test_wrap_content():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap()
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."
    
'''return exception for an unwrapped content'''
def test_wrap_content():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

