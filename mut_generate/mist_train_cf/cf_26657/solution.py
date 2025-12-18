"""
QUESTION:
Implement a Python decorator named `verbose_log` that logs function calls based on the presence of the 'VERBOSE' environment variable. The decorator should log the current timestamp, function name, and function arguments if 'VERBOSE' is set. If 'VERBOSE' is not set, the decorator should not log anything. The decorator should work for functions with any number of positional and keyword arguments and not modify the behavior of the original function.
"""

import os
from datetime import datetime

def verbose_log(func):
    def wrapper(*args, **kwargs):
        if os.getenv('VERBOSE'):
            print(datetime.now(), func.__name__, 'called with args:', args, 'and kwargs:', kwargs)
        return func(*args, **kwargs)
    return wrapper