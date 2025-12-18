"""
QUESTION:
Implement a class `CustomException` that inherits from the built-in `Exception` class. The `CustomException` class should have an `encode` method that returns a dictionary containing the exception message and any additional keyword arguments passed to the constructor.

The `encode` method should return a dictionary where the key "details" maps to the exception message and any additional keyword arguments are included as key-value pairs. 

Additionally, implement a method `format_output` that takes an instance with attributes "details", "model", and "response", and returns a formatted string containing the details, expected value, and actual value from the instance. The formatted string should be in the format "Details: {details}\nExpected: {model}\nActual: {response}".
"""

class CustomException(Exception):
    def __init__(self, message, **kwargs):
        self.kwargs = kwargs
        self.message = message

    def encode(self):
        encoded = {"details": self.message}
        encoded.update(self.kwargs)
        return encoded


def format_output(instance):
    return f"Details: {instance.details}\nExpected: {str(instance.model)}\nActual: {instance.response}"