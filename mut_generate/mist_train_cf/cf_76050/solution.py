"""
QUESTION:
Create a Python program that implements a decorator named `exceptionDecorator` to catch exceptions and demonstrate the use of `@staticmethod` and `@classmethod` decorators. The `exceptionDecorator` should handle exceptions that occur within the decorated methods.
"""

def exceptionDecorator(func):
    def innerFunction(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
    return innerFunction