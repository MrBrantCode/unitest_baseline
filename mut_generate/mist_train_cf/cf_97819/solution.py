"""
QUESTION:
Write a Python function `avg_salary_by_gender_and_department` that takes a table of employee details with columns "Name", "Age", "Gender", "Salary", and "Department" and returns a dictionary with the average salary for each gender categorized by department. The input table is a list of dictionaries, where each dictionary represents an employee. The output dictionary should have tuples of department and gender as keys and the corresponding average salary as values, rounded to 2 decimal places.
"""

def avg_salary_by_gender_and_department(table):
    """
    This function calculates the average salary for each gender categorized by department.

    Args:
    table (list): A list of dictionaries, where each dictionary represents an employee.
                  Each dictionary should have the keys "Name", "Age", "Gender", "Salary", and "Department".

    Returns:
    dict: A dictionary with tuples of department and gender as keys and the corresponding average salary as values, rounded to 2 decimal places.
    """

    # Create an empty dictionary to store the sum of salaries and count of employees for each department and gender
    avg_salaries = {}
    for row in table:
        department = row['Department']
        gender = row['Gender']
        salary = row['Salary']
        
        # If the department and gender are already in the dictionary, add the salary to the total and increment the count
        if (department, gender) in avg_salaries:
            avg_salaries[(department, gender)][0] += salary
            avg_salaries[(department, gender)][1] += 1
        # If the department and gender are not in the dictionary, add them with the salary and a count of 1
        else:
            avg_salaries[(department, gender)] = [salary, 1]

    # Calculate the average salary for each department and gender
    for key in avg_salaries:
        avg_salaries[key] = round(avg_salaries[key][0] / avg_salaries[key][1], 2)

    return avg_salaries