"""
QUESTION:
Create a function named `determine_discount` that takes an age and a boolean indicating whether the user is an employee as input. The function should use two boolean flag variables to control the flow of the program and handle multiple conditions at once. The function should return a string indicating whether the user is eligible for a special discount, an adult discount, an employee discount, or no discount at all. The function should not take any other inputs and the input values should be hardcoded in the test case.
"""

def determine_discount(age, is_employee):
    """
    Determine whether a user is eligible for a special discount, an adult discount, an employee discount, or no discount at all.

    Parameters:
    age (int): The age of the user.
    is_employee (bool): A boolean indicating whether the user is an employee.

    Returns:
    str: A string indicating the type of discount the user is eligible for.
    """

    # Determine whether the user is an adult
    is_adult = age >= 18

    # Check the status of the user based on flag variables
    if is_adult and is_employee:
        return "You are eligible for a special discount."
    elif is_adult and not is_employee:
        return "You are eligible for an adult discount."
    elif not is_adult and is_employee:
        return "You are eligible for an employee discount."
    else:
        return "You are not eligible for any discount."