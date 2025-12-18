"""
QUESTION:
Create a function `process_time_status(time_value, did_change)` that takes two parameters: a time value to be processed and a boolean indicating whether a change occurred. The function should raise an `OutsideTimeBounds` exception if the time value is outside the bounds (assuming lower_bound and upper_bound are predefined). Otherwise, return a status code of 200 with a status type of `OK` if did_change is True, and a status code of 440 with a status type of `NOOP` if did_change is False. Use the given `with_status` function and `StatusType` enum to return the status code and type.
"""

from enum import Enum

class StatusType(Enum):
    ERROR = "ERROR"
    OK = "OK"
    NOOP = "NOOP"

class OutsideTimeBounds(Exception):
    pass

def with_status(data, code, status_type):
    return data, code, status_type

def entrance(time_value, did_change, lower_bound, upper_bound):
    if time_value < lower_bound or time_value > upper_bound:
        raise OutsideTimeBounds
    else:
        if did_change:
            return with_status(None, 200, StatusType.OK)
        else:
            return with_status(None, 440, StatusType.NOOP)