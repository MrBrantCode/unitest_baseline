"""
QUESTION:
Implement a function named `set_operations` that takes two lists of employees as input, one for the engineering department and one for the marketing department, and returns three sets: common employees who work in both departments, employees who work only in the engineering department, and employees who work only in the marketing department.
"""

def set_operations(engineering_department, marketing_department):
    """
    This function takes two lists of employees as input, one for the engineering department and one for the marketing department.
    It returns three sets: common employees who work in both departments, employees who work only in the engineering department,
    and employees who work only in the marketing department.

    Args:
        engineering_department (list): A list of employees in the engineering department.
        marketing_department (list): A list of employees in the marketing department.

    Returns:
        tuple: A tuple containing three sets: common employees, engineering only employees, and marketing only employees.
    """

    # Convert the input lists to sets
    engineering_set = set(engineering_department)
    marketing_set = set(marketing_department)

    # Find the common employees using the intersection operation
    common_employees = engineering_set.intersection(marketing_set)

    # Find the employees exclusive to the engineering department using the difference operation
    engineering_only_employees = engineering_set.difference(marketing_set)

    # Find the employees exclusive to the marketing department using the difference operation
    marketing_only_employees = marketing_set.difference(engineering_set)

    return common_employees, engineering_only_employees, marketing_only_employees