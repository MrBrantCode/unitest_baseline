"""
QUESTION:
Implement a function named 'assignDayValue' that takes two parameters: a string representing a day of the week and a boolean value. Validate the input to only accept seven days of the week (in string format) and boolean values. If invalid inputs are provided, return an appropriate error message. Create a variable with the name as the day of the week and assign it the given boolean value. 

Note: The function should handle the creation of the variable in a way that simulates dynamic variable creation, considering the limitations and security concerns of directly creating dynamic variables in languages like Python.
"""

def assignDayValue(day, value):
    """
    Assign a boolean value to a dynamic variable with the name of a day of the week.

    Args:
    day (str): A string representing a day of the week.
    value (bool): A boolean value.

    Returns:
    str: An error message if the input is invalid, otherwise a success message.
    """

    daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    if day not in daysOfWeek:
        return "Invalid day of the week."

    if type(value) != bool:
        return "Invalid boolean value."

    dynamicVariables = {}  # Dictionary to store dynamic variables
    dynamicVariables[day] = value
    return f"{day} has been set to {value}."