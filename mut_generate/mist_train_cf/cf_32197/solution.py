"""
QUESTION:
Implement a function `deduct_salary` that takes an initial salary and a list of website names as input, applies deductions based on the website names, and returns the updated salary or a message if the salary becomes zero or negative. The deductions are as follows: Facebook ($150), Instagram ($100), and Reddit ($50). If the salary becomes zero or negative, return "You have lost your salary."
"""

def deduct_salary(salary, tabs):
    """
    This function deducts salary based on the website names.
    
    Args:
    salary (float): The initial salary.
    tabs (list): A list of website names.
    
    Returns:
    float or str: The updated salary or a message if the salary becomes zero or negative.
    """
    deductions = {
        "Facebook": 150,
        "Instagram": 100,
        "Reddit": 50
    }
    
    for tab in tabs:
        if tab in deductions:
            salary -= deductions[tab]
        if salary <= 0:
            return "You have lost your salary."
    
    return salary