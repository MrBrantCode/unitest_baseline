"""
QUESTION:
Write a function called `get_average_salary` to calculate the average salary of employees who meet the following conditions: at least 5 years with the company, job title of "Senior Software Engineer", and a performance rating of at least 4. The input collection is expected to contain employee documents with the fields `yearsWithCompany`, `jobTitle`, `performanceRating`, and `salary`. The function should return the average salary of the qualified employees.
"""

def get_average_salary(employees):
    """
    Calculate the average salary of employees who are Senior Software Engineers 
    with at least 5 years of service and a performance rating of at least 4.

    Args:
    employees (list): A list of employee dictionaries containing 'yearsWithCompany', 
                     'jobTitle', 'performanceRating', and 'salary' keys.

    Returns:
    float: The average salary of the qualified employees.
    """
    qualified_employees = [
        employee for employee in employees 
        if employee['yearsWithCompany'] >= 5 and 
           employee['jobTitle'] == "Senior Software Engineer" and 
           employee['performanceRating'] >= 4
    ]

    if qualified_employees:
        return sum(employee['salary'] for employee in qualified_employees) / len(qualified_employees)
    else:
        return 0