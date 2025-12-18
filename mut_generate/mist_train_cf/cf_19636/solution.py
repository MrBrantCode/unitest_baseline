"""
QUESTION:
Implement a function `bitmap_indexing` that takes in a list of employees where each employee is a dictionary containing 'Department' and 'Salary' information, and returns a list of employees in the "Sales" department with a salary greater than 50000. The function should utilize bitmap indexing to optimize the query performance.
"""

def bitmap_indexing(employees):
    sales_bitmap = [1 if employee['Department'] == 'Sales' else 0 for employee in employees]
    salary_bitmap = [1 if employee['Salary'] > 50000 else 0 for employee in employees]
    result_bitmap = [sales_bitmap[i] & salary_bitmap[i] for i in range(len(employees))]
    return [employee for employee, bit in zip(employees, result_bitmap) if bit == 1]