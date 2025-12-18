"""
QUESTION:
Write a function `higher_than_average` to find the names of all employees with a salary higher than the average salary of all employees and more than 5 years of experience.
"""

def higher_than_average(employees):
    """
    Returns a list of names of employees with a salary higher than the average salary of all employees and more than 5 years of experience.

    Args:
        employees (list): A list of dictionaries containing employee information.
                         Each dictionary should have 'Name', 'Salary', and 'Years_of_Experience' keys.

    Returns:
        list: A list of employee names.
    """
    if not employees:
        return []

    total_salary = sum(employee['Salary'] for employee in employees)
    average_salary = total_salary / len(employees)

    return [employee['Name'] for employee in employees 
            if employee['Salary'] > average_salary and employee['Years_of_Experience'] > 5]