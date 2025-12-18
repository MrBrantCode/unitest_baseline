"""
QUESTION:
Design an Employee class with a method to calculate the average salary of employees within a given department. The class should allow for efficient search functionality to find employees based on different criteria such as department, salary range, performance rating, and age range. The average salary calculation should be based on the salaries of employees within the specified department. The class should also store information about employees, including their name, telephone number, age, address, job title, department, salary, and performance reviews.
"""

def calculate_average_salary(employees, department):
    """
    Calculate the average salary of employees within a given department.
    
    Args:
        employees (list): A list of dictionaries containing employee information.
        department (str): The department for which to calculate the average salary.
    
    Returns:
        float: The average salary of employees in the specified department.
    """
    total_salary = 0
    employee_count = 0
    
    for employee in employees:
        if employee['department'] == department:
            total_salary += employee['salary']
            employee_count += 1
    
    if employee_count == 0:
        return 0
    else:
        return total_salary / employee_count

# Note: The employee data structure is assumed to be a list of dictionaries, where each dictionary represents an employee with keys for name, telephone number, age, address, job title, department, salary, and performance reviews.