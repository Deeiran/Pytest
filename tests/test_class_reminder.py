
import pytest
from lib.class_reminder import *
''' Return a reminder without exception'''
def test_reminder_with_exception():
    reminder = Reminder("adam")
    reminder.remind_me_to("welcome Home!")
    result = reminder.remind()
    assert result == "adam, welcome Home!"


''' Return a reminder with exception'''
def test_reminder_with_exception():
    reminder = Reminder("adam")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"
