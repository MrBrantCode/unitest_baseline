"""
QUESTION:
Write a function `count_subordinates(json_obj, emp_id)` that takes in a dictionary representing a company's employee hierarchy and an employee ID, and returns the total number of subordinates (both direct and indirect) for the given employee. The dictionary's keys are the employee IDs and the values are dictionaries containing the employee's name and a list of their subordinates' IDs. The function should return 0 if the given employee ID does not exist in the dictionary.

Input: 
- `json_obj`: a dictionary representing the employee hierarchy (1 <= len(json_obj) <= 1000)
- `emp_id`: a string representing the employee ID (1 <= len(emp_id) <= 10)

Output: 
- An integer representing the total number of subordinates for the given employee ID.
"""

def count_subordinates(json_obj: dict, emp_id: str) -> int:
    if emp_id not in json_obj:
        return 0
    
    total_subordinates = len(json_obj[emp_id]["subordinates"])
    for subordinate_id in json_obj[emp_id]["subordinates"]:
        total_subordinates += count_subordinates(json_obj, subordinate_id)
    
    return total_subordinates