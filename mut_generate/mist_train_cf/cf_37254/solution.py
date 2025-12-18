"""
QUESTION:
Implement a function `add_numbers(a, b)` that calculates the sum of two numbers `a` and `b`. The function should use the Python `logging` module to log an INFO-level message to the console indicating the addition operation being performed, including the values of `a` and `b`. The log message format should include the log level, timestamp, and the message itself. The function should return the sum of `a` and `b`.
"""

import logging

def add_numbers(a, b):
    logging.info(f"Adding {a} to {b}")
    return a + b