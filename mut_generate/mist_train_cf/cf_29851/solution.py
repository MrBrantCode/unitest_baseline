"""
QUESTION:
Write a function named `highest_avg_salary_increase` that takes a list of tuples as input. Each tuple represents an employee's data and contains four elements: the employee's name (string), department (string), current salary (integer), and previous salary (integer). The function should calculate the average salary increase for each department and return the department with the highest average salary increase.
"""

def highest_avg_salary_increase(data):
    department_salary_increase = {}
    department_count = {}
    
    for _, department, current_salary, previous_salary in data:
        increase = current_salary - previous_salary
        if department in department_salary_increase:
            department_salary_increase[department] += increase
            department_count[department] += 1
        else:
            department_salary_increase[department] = increase
            department_count[department] = 1
    
    max_avg_increase = 0
    max_avg_department = ""
    
    for department in department_salary_increase:
        avg_increase = department_salary_increase[department] / department_count[department]
        if avg_increase > max_avg_increase:
            max_avg_increase = avg_increase
            max_avg_department = department
    
    return max_avg_department