"""
QUESTION:
Implement a function named `check_exception_chain` that takes two parameters: `err` of type `Exception` and `object_type` of type `Type`. The function should return `True` if the exception chain starting from `err` includes an exception of type `object_type`, and `False` otherwise. The exception chain can be of arbitrary length, and `object_type` is guaranteed to be a valid exception type.
"""

from typing import Type

def check_exception_chain(err: Exception, object_type: Type) -> bool:
    if isinstance(err, object_type):
        return True
    elif err.__cause__ is not None:
        return check_exception_chain(err.__cause__, object_type)
    elif err.__context__ is not None:
        return check_exception_chain(err.__context__, object_type)
    else:
        return False