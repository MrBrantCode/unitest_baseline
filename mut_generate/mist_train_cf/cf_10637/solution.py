"""
QUESTION:
Implement a function `normalize_data` that takes a dictionary representing a table with 'EmployeeID', 'Name', and 'Department' as keys and returns two separate dictionaries representing the 'Employees' and 'Departments' tables after normalization, following the second normal form (2NF). The input dictionary should be normalized to eliminate data redundancy. The 'Employees' table should have 'EmployeeID' and 'Name' columns, while the 'Departments' table should have 'DepartmentID' and 'Department' columns. The 'Department' column in the 'Employees' table should be replaced with a 'DepartmentID' that references the corresponding department in the 'Departments' table.
"""

def normalize_data(data):
    """
    Normalize the input data into two separate dictionaries representing the 'Employees' and 'Departments' tables.

    Args:
        data (dict): A dictionary representing a table with 'EmployeeID', 'Name', and 'Department' as keys.

    Returns:
        tuple: Two dictionaries representing the 'Employees' and 'Departments' tables after normalization.
    """

    # Initialize empty dictionaries to store the normalized data
    employees = {}
    departments = {}

    # Initialize a counter to generate unique DepartmentIDs
    department_id = 1

    # Iterate over each employee in the input data
    for employee_id, name, department in zip(data['EmployeeID'], data['Name'], data['Department']):
        # Add the employee to the 'Employees' table
        employees[employee_id] = {'Name': name, 'DepartmentID': None}

        # Check if the department already exists in the 'Departments' table
        if department not in departments.values():
            # If not, add the department to the 'Departments' table with a unique DepartmentID
            departments[department_id] = department
            # Update the DepartmentID in the 'Employees' table
            employees[employee_id]['DepartmentID'] = department_id
            # Increment the DepartmentID counter
            department_id += 1
        else:
            # If the department already exists, find its DepartmentID and update the 'Employees' table
            department_id_key = [key for key, value in departments.items() if value == department][0]
            employees[employee_id]['DepartmentID'] = department_id_key

    return employees, departments