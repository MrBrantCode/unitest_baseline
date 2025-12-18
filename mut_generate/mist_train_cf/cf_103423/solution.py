"""
QUESTION:
Create a function called `createValidEmployee` that takes an object with `name`, `age`, and `salary` properties as input. The function should return a new object with the same properties if the employee's `name` is at least 5 characters long and their `salary` is a positive integer. Otherwise, return a message indicating that the employee is invalid.
"""

def createValidEmployee(employee):
    """
    Returns a new employee object if the employee's name is at least 5 characters long and their salary is a positive integer.
    Otherwise, returns a message indicating that the employee is invalid.

    Args:
        employee (dict): A dictionary containing 'name', 'age', and 'salary' properties.

    Returns:
        dict or str: A new employee object or an error message.
    """
    if len(employee['name']) >= 5 and isinstance(employee['salary'], int) and employee['salary'] > 0:
        return {'name': employee['name'], 'age': employee['age'], 'salary': employee['salary']}
    else:
        return "Invalid employee"