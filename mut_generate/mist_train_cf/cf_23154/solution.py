"""
QUESTION:
Create a function `get_veteran_employees` that takes no arguments. This function should return a list of employees who meet the following criteria: they have completed more than 20 years of service, have received at least one promotion, and have worked in multiple departments. The output should include the employee's ID, name, a list of department names they have worked in, and the total number of promotions they have received.
"""

def get_veteran_employees(employees, departments, promotions):
    """
    Returns a list of veteran employees who have completed more than 20 years of service, 
    received at least one promotion, and have worked in multiple departments.

    Args:
    employees (list): A list of employee objects or dictionaries containing 'employee_id', 'employee_name', and 'years_of_service'.
    departments (list): A list of department objects or dictionaries containing 'employee_id' and 'department_name'.
    promotions (list): A list of promotion objects or dictionaries containing 'employee_id' and 'promotion_id'.

    Returns:
    list: A list of veteran employee objects or dictionaries containing 'employee_id', 'employee_name', 
          'departments', and 'total_promotions'.
    """
    
    # First, filter the employees who have completed more than 20 years of service
    veteran_employees = [e for e in employees if e['years_of_service'] > 20]
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each veteran employee
    for employee in veteran_employees:
        # Filter the departments the employee has worked in
        employee_departments = [d['department_name'] for d in departments if d['employee_id'] == employee['employee_id']]
        
        # Filter the promotions the employee has received
        employee_promotions = [p for p in promotions if p['employee_id'] == employee['employee_id']]
        
        # Check if the employee has received at least one promotion and has worked in multiple departments
        if len(employee_promotions) > 0 and len(employee_departments) > 1:
            # Append the employee's information to the result list
            result.append({
                'employee_id': employee['employee_id'],
                'employee_name': employee['employee_name'],
                'departments': employee_departments,
                'total_promotions': len(employee_promotions)
            })
    
    return result