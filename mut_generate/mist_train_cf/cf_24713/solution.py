"""
QUESTION:
Write a function `second_highest_salary` to find the second-highest salary from a given list of employee salaries. The function should return the second-highest salary if it exists, otherwise return `None`. The input list may contain duplicate salaries.
"""

def second_highest_salary(salaries):
    """
    This function finds the second-highest salary from a given list of employee salaries.
    
    Args:
        salaries (list): A list of employee salaries.
    
    Returns:
        The second-highest salary if it exists, otherwise None.
    """
    unique_salaries = sorted(set(salaries), reverse=True)
    
    # Check if there are at least two unique salaries
    if len(unique_salaries) < 2:
        return None
    
    # Return the second-highest salary
    return unique_salaries[1]