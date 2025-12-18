"""
QUESTION:
Create a function `construct_employee` to design an object representing an employee. The object should contain properties for the employee's name, phone number, salary, and a list of previous job positions. Each job position should include the company name, job title, start date, and end date.
"""

def construct_employee(name, phone_number, salary, previous_job_positions):
    """
    Creates an object representing an employee.

    Args:
    name (str): The employee's name.
    phone_number (str): The employee's phone number.
    salary (float): The employee's salary.
    previous_job_positions (list): A list of dictionaries containing information about the employee's previous job positions.

    Returns:
    dict: An object representing the employee.
    """
    return {
        "name": name,
        "phoneNumber": phone_number,
        "salary": salary,
        "previousJobPositions": previous_job_positions
    }