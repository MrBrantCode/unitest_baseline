"""
QUESTION:
Write a function `avg_without_min_max(a_list)` that calculates the average of the numbers in the list `a_list`, excluding the minimum and maximum values. The list must contain at least 3 distinct numbers.
"""

def avg_without_min_max(a_list):
    # Check if there are at least 3 distinct numbers
    if len(set(a_list)) < 3:
        return "List must contain at least 3 distinct numbers."
    
    # Remove the min and max value
    a_list.remove(min(a_list))
    a_list.remove(max(a_list))
    
    # Compute and return the average of the remaining numbers
    return sum(a_list) / len(a_list)