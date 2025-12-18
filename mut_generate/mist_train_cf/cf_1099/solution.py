"""
QUESTION:
Create a function `filter_and_sort_employees` that takes a list of employee data as input, where each employee is a dictionary with keys 'Name', 'Salary', 'Age', and 'Department'. The function should filter the employees to include only those with a salary between 40,000 and 50,000, an age between 30 and 40, and a department of "Sales". Then, it should calculate the total salary of the filtered employees and return a tuple containing the total salary and a list of the top 5 employees' names and salaries, sorted by salary in descending order.
"""

def filter_and_sort_employees(employees):
    """
    Filter employees based on salary, age, and department, 
    calculate total salary, and return top 5 employees' names and salaries.

    Args:
        employees (list): A list of employee data, where each employee is a dictionary.

    Returns:
        tuple: A tuple containing the total salary and a list of the top 5 employees' names and salaries.
    """

    # Filter employees based on criteria
    filtered_employees = [emp for emp in employees 
                          if 40000 <= int(emp['Salary']) <= 50000 
                          and 30 <= int(emp['Age']) <= 40 
                          and emp['Department'] == "Sales"]

    # Calculate total salary of the filtered employees
    total_salary = sum(int(emp['Salary']) for emp in filtered_employees)

    # Sort and get the top 5 employees' names and salaries
    top_employees = sorted(filtered_employees, key=lambda emp: int(emp['Salary']), reverse=True)[:5]
    top_employees = [{'Name': emp['Name'], 'Salary': emp['Salary']} for emp in top_employees]

    return total_salary, top_employees