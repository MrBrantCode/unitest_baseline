"""
QUESTION:
Create a function called `generate_employee_table` that takes a list of dictionaries as input. Each dictionary should contain information about an employee, including their name, age, and designation. 

The function should calculate the years of experience for each employee by subtracting their age from the current year and add this information to the dictionary. It should then sort the list of employees in ascending order based on their years of experience.

The function should also calculate the total number of employees, the average age of the employees, and the number of employees in each designation. 

Finally, the function should identify the oldest employee and return the list of employees along with the total number of employees, the average age, the designation count, and the oldest employee. 

The function should not take any additional arguments other than the list of employees. The current year should be assumed to be 2022.
"""

def generate_employee_table(employees):
    """
    This function generates an employee table with additional information.

    Args:
    employees (list): A list of dictionaries containing employee information.

    Returns:
    A dictionary containing the list of employees, total number of employees, 
    average age, designation count, and the oldest employee.
    """

    # Calculate years of experience and sort the employees based on it
    current_year = 2022
    for employee in employees:
        employee["years_of_experience"] = current_year - employee["age"]
    sorted_employees = sorted(employees, key=lambda x: x["years_of_experience"])

    # Count the total number of employees
    total_employees = len(sorted_employees)

    # Calculate the average age of the employees
    total_age = sum([employee["age"] for employee in sorted_employees])
    average_age = total_age / total_employees

    # Count the number of employees in each designation
    designation_count = {}
    for employee in sorted_employees:
        designation = employee["designation"]
        designation_count[designation] = designation_count.get(designation, 0) + 1

    # Find the oldest employee
    oldest_employee = max(sorted_employees, key=lambda x: x["age"])

    return {
        "employees": sorted_employees,
        "total_employees": total_employees,
        "average_age": average_age,
        "designation_count": designation_count,
        "oldest_employee": oldest_employee
    }