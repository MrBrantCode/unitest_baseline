"""
QUESTION:
Create a function `handle_exceptions` that takes a function `func` as an argument and returns a wrapper function. The wrapper function should handle exceptions raised by `func`, logging them to a file and printing a corresponding error message. The exceptions to be handled are `ValueError`, `DivisionError`, and a general `Exception`. The function should also include a finally block to execute after handling any exceptions. The exceptions should be logged to a file named "sample.log" with the logging level set to INFO.
"""

import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            logging.error(f"ValueError: {str(e)}")
            print("ValueError occurred. Check the log for more information.")
        except Exception as e:
            if isinstance(e, ZeroDivisionError):
                logging.error(f"DivisionError: {str(e)}")
                print("DivisionError occurred. Check the log for more information.")
            else:
                logging.error(f"Exception: {str(e)}")
                print("An unexpected error occurred. Check the log for more information.")
        finally:
            print("Operation completed.")
    return wrapper