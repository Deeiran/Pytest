

from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("senthoo")
    reminder.remind_me_to("go to makers")
    result = reminder.remind()
    assert result == "go to makers, senthoo!"

# We would typically have a number of these examples.