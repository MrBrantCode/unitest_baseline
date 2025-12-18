"""
QUESTION:
Write a function `cumulative_significance(employee_data, employee_id, target_level)` that calculates the cumulative significance score of the employee and all their subordinates up to the specified hierarchical level. 

Each employee in `employee_data` is represented as a list `[id, significance, level, subordinates]`, where `id` is a unique identifier, `significance` is the employee's significance score, `level` is their position in the organizational hierarchy, and `subordinates` is a list of ids of their immediate subordinates. The `employee_id` and `target_level` are given as input. 

The function should return the cumulative significance score as an integer. Note that the hierarchical level of an employee is a positive integer with the leader occupying the lowest level, and the maximum number of employees and maximum hierarchical level will not exceed 2000 and the total number of employees respectively.
"""

def cumulative_significance(employee_data, employee_id, target_level):
    # Creation of a dictionary for quick access to employees' information using their unique ids
    ids_to_index = {data[0] : i for i, data in enumerate(employee_data)}
    
    # Initialize the cumulative significance score to 0
    cum_sig_score = 0

    # Depth-First Search to traverse the organization hierarchy
    def DFS(emp_id, level):
        nonlocal cum_sig_score
        index = ids_to_index[emp_id]
        
        # Add the employee significance score to the cumulative score if they're within the target level
        if level <= target_level:
            cum_sig_score += employee_data[index][1]
        
        # Continue the depth-first search with the subordinates if the next level is within the target level
        if level + 1 <= target_level:
            for sub_id in employee_data[index][3]:
                DFS(sub_id, level + 1)

    # Starting the Depth-First Search with the given employee id
    DFS(employee_id, employee_data[ids_to_index[employee_id]][2])
    
    return cum_sig_score