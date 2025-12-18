"""
QUESTION:
Create a function named `power_func` that takes a required `number` parameter and an optional `power` parameter (defaulting to 3 if not provided). The function should first validate that the input `number` is a valid numerical value. If the input is invalid, return an error message. Otherwise, raise the valid numerical `number` to the specified `power` and return the result.
"""

def power_func(number, power=3):
    try:
        float_number = float(number)
    except ValueError:
        return "Error: The input is not a valid numerical value!"
    return pow(float_number, power)