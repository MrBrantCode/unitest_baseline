"""
QUESTION:
Write a function named `callback_function` that takes a string, an integer, and a boolean as arguments. The function should return a callable that stores the input and emits it when triggered, but only if the boolean flag is True and the callable has not been triggered before.
"""

def callback_function(input_string: str, input_number: int, input_flag: bool) -> callable:
    called = False
    stored_data = None

    def callback() -> None:
        nonlocal called, stored_data
        if not called and input_flag:
            called = True
            stored_data = (input_string, input_number, input_flag)
            print("Callback triggered!")
            print("Stored data:", stored_data)
        else:
            print("Callback cannot be triggered. Flag must be set to True before triggering.")
            
    return callback