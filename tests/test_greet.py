from lib.greet import *
def test_greet_print_hello_with_given_name():
    result = greet("Sarah")
    assert result == "Hello, Sarah!"