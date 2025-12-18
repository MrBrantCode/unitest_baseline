"""
QUESTION:
Write a function `calc_salary_detail` that takes a JSON string `nested_json_string` as input, where the JSON string represents a dictionary containing a list of employees with their department and salary. The function should calculate and return the maximum, minimum, and average salary for each department. The returned result should be a dictionary where each key is a department and the corresponding value is another dictionary with the keys 'max', 'min', and 'avg' representing the maximum, minimum, and average salary, respectively.
"""

import json
from collections import defaultdict

def calc_salary_detail(nested_json_string):
    # Parse JSON and convert it into Python dictionary
    data = json.loads(nested_json_string)
    
    # Initialize defaultdict to store salary details
    salary_info = defaultdict(list)
    
    # Calculate salary details
    for employee in data["employees"]:
        salary_info[employee["department"]].append(employee["salary"])
        
    # Store calculated max, min, and average values
    for department, salaries in salary_info.items():
        max_salary = max(salaries)
        min_salary = min(salaries)
        avg_salary = sum(salaries) / len(salaries)
        salary_info[department] = {"max": max_salary, "min": min_salary, "avg": avg_salary}

    return salary_info