"""
QUESTION:
Write a function `generate_summary_report(employee_records)` that takes a list of dictionaries `employee_records` as input, where each dictionary contains the keys "name", "department", "salary", and "joining_year". The function should calculate and return a dictionary containing the average salary (rounded to the nearest integer) and total number of employees for each department.
"""

def generate_summary_report(employee_records):
    department_summary = {}
    department_count = {}
    
    for record in employee_records:
        department = record["department"]
        salary = record["salary"]
        
        if department in department_summary:
            department_summary[department] += salary
            department_count[department] += 1
        else:
            department_summary[department] = salary
            department_count[department] = 1
    
    for department in department_summary:
        average_salary = round(department_summary[department] / department_count[department])
        department_summary[department] = {
            "average_salary": average_salary,
            "total_employees": department_count[department]
        }
    
    return department_summary