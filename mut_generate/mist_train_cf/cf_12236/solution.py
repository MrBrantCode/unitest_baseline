"""
QUESTION:
Implement a function `exception_handler` that accepts a function as an argument and returns a wrapper function. The returned wrapper function should catch and handle any exceptions raised by the input function. If an exception occurs, the wrapper function should log the error message and continue executing.
"""

import logging
import functools

def exception_handler(func):
    """
    A decorator function to catch and handle exceptions raised by the input function.
    
    Args:
        func: The input function to be wrapped.
    
    Returns:
        A wrapper function that catches and handles exceptions.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
    return wrapper