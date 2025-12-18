"""
QUESTION:
Write a SQL query to find the third highest salary in the Employee table. The Employee table contains employee information with a Salary column. The query should return the third highest unique salary, and if there are less than three unique salaries, it should return null or the highest salary available.
"""

def third_highest_salary(salaries):
    """
    Returns the third highest unique salary from a list of salaries.
    
    If there are less than three unique salaries, returns None or the highest salary available.
    
    Parameters:
    salaries (list): A list of salaries
    
    Returns:
    int or None: The third highest unique salary or None
    """
    unique_salaries = sorted(set(salaries))
    if len(unique_salaries) < 3:
        return unique_salaries[-1] if unique_salaries else None
    return unique_salaries[-3]