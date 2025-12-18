"""
QUESTION:
Write a function `callback_function` that takes in a string, an integer, and a boolean flag, and returns a callback function that stores the input and emits it when triggered. The callback function can only be triggered once and only if the boolean flag is True.
"""

def callback_function(input_string: str, input_number: int, input_flag: bool) -> callable:
    called = False
    stored_data = (input_string, input_number, input_flag)

    def callback() -> None:
        nonlocal called
        if not called and input_flag:
            called = True
            print("Callback triggered!")
            print("Stored data:", stored_data)
        else:
            print("Callback cannot be triggered. Flag must be set to True before triggering.")
            
    return callback