"""
QUESTION:
Implement a function called `employee_department_analysis` that takes two lists of employee names, `engineering_department` and `marketing_department`, as input and returns a dictionary containing three keys: `common_employees`, `engineering_only_employees`, and `marketing_only_employees`. The values for these keys should be sets of employee names that are common to both departments, exclusive to the engineering department, and exclusive to the marketing department, respectively.
"""

def employee_department_analysis(engineering_department, marketing_department):
    """
    This function takes two lists of employee names as input and returns a dictionary containing three keys: 
    'common_employees', 'engineering_only_employees', and 'marketing_only_employees'.

    Args:
    engineering_department (list): A list of employee names in the engineering department.
    marketing_department (list): A list of employee names in the marketing department.

    Returns:
    dict: A dictionary containing three keys: 'common_employees', 'engineering_only_employees', and 'marketing_only_employees'.
    """

    # Convert the lists to sets for efficient set operations
    engineering_set = set(engineering_department)
    marketing_set = set(marketing_department)

    # Find common employees using set intersection
    common_employees = engineering_set.intersection(marketing_set)

    # Find employees exclusive to the engineering department using set difference
    engineering_only_employees = engineering_set.difference(marketing_set)

    # Find employees exclusive to the marketing department using set difference
    marketing_only_employees = marketing_set.difference(engineering_set)

    # Return a dictionary with the required information
    return {
        'common_employees': common_employees,
        'engineering_only_employees': engineering_only_employees,
        'marketing_only_employees': marketing_only_employees
    }