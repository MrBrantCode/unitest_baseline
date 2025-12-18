"""
QUESTION:
Implement a function `custom_sort_employees(employees)` that sorts a list of employee objects in the following order: 
- descending order by department 
- ascending order by position within each department 
- ascending order by full name within each department and position. 

The input list contains dictionaries representing employee objects with 'department', 'position', and 'full_name' attributes.
"""

def custom_sort_employees(employees):
    return sorted(employees, key=lambda emp: (-emp['department'], emp['position'], emp['full_name']))