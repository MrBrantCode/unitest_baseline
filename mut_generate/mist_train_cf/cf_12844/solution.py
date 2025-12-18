"""
QUESTION:
Write a function `average_female_height` that calculates the average height of female employees who have worked in the company for at least 5 years. The function should take a list of employee data, where each employee is represented as a dictionary with keys 'height', 'tenure', and 'gender'. The function should return the average height as a float.
"""

def average_female_height(employees):
    """
    This function calculates the average height of female employees who have worked 
    in the company for at least 5 years.

    Args:
        employees (list): A list of employee data, where each employee is represented 
            as a dictionary with keys 'height', 'tenure', and 'gender'.

    Returns:
        float: The average height of female employees who have worked in the company 
            for at least 5 years.
    """

    # Filter the employees to only include females who have worked for at least 5 years
    eligible_employees = [employee for employee in employees if employee['gender'] == 'female' and employee['tenure'] >= 5]

    # Check if there are any eligible employees
    if not eligible_employees:
        return 0  # or raise an exception, depending on the desired behavior

    # Calculate the sum of the heights of the eligible employees
    total_height = sum(employee['height'] for employee in eligible_employees)

    # Calculate the average height
    average_height = total_height / len(eligible_employees)

    return average_height