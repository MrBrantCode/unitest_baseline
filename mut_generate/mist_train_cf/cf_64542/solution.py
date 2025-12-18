"""
QUESTION:
Create a Python decorator named `modify_return_val_decorator` that takes a function as input, catches any exceptions that occur during the execution of the function, and modifies the function's return value by prefixing it with the string "Modified: ". The decorator should return the modified function.
"""

def modify_return_val_decorator(func):
    def inner_function(*args, **kwargs):
        try:
            original_result = func(*args, **kwargs)
        except Exception as e:
            print(f"Error occurred in function: {str(e)}")
            return None
        return "Modified: " + str(original_result)

    return inner_function