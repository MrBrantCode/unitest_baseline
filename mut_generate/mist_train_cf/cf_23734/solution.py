"""
QUESTION:
Write a function `getSecondHighestSalary` to retrieve the second highest salary from a database table 'Employees'. The table is assumed to have a column named 'salary' containing the employee salaries. If there are duplicate highest salaries, consider the next distinct highest value as the second highest salary. If there is only one unique salary in the table or all salaries are the same, return `NULL` as the second highest salary does not exist.
"""

def getSecondHighestSalary(salaries):
    """
    Retrieves the second highest salary from a list of salaries.

    Args:
    salaries (list): A list of employee salaries.

    Returns:
    int or None: The second highest salary if it exists, otherwise None.
    """
    distinct_salaries = sorted(set(salaries))
    if len(distinct_salaries) < 2:
        return None
    else:
        return distinct_salaries[-2]