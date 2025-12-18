"""
QUESTION:
Write a query named 'getNthHighestSalary' to find the nth highest salary from the table Employees, where n is a user-inputted parameter. The query should return the correct result even if multiple employees have the same salary.
"""

def getNthHighestSalary(n, salaries):
    """
    This function returns the nth highest salary from the given list of salaries.

    Args:
        n (int): The position of the salary to be found.
        salaries (list): A list of salaries.

    Returns:
        int or None: The nth highest salary if it exists, otherwise None.
    """
    if n < 1:
        return None
    distinct_salaries = sorted(set(salaries), reverse=True)
    if n > len(distinct_salaries):
        return None
    return distinct_salaries[n-1]