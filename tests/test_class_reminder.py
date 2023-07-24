import pytest
from lib.class_reminder import *
''' Return a reminder without exception'''
def test_reminder_with_exception():
    reminder = Reminder("Adam")
    reminder.remind_me_to("Wake me")
    result = reminder.remind()
    assert result == "Wake me, Adam"

''' Return a reminder with exception'''
def test_reminder_with_exception():
    reminder = Reminder("Adam")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"