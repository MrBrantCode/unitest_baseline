"""
QUESTION:
Implement a function named `handle_error` that uses try-except blocks to catch and handle exceptions in Python. The function should be able to execute a given block of code, handle any exceptions that occur, and perform any necessary cleanup after execution.
"""

def handle_error(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Add cleanup code here if necessary
        pass