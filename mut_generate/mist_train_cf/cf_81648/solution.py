"""
QUESTION:
Create a function named `sort_by_priority` that takes two lists: a list of fruit names as strings and a list of their respective priority categories as integers, where 1 is the highest priority and n is the lowest. The function should return a single string containing the fruit names sorted by their priority categories first and then in alphabetical order within each category. The input lists will have the same length, and each fruit name will be paired with a priority category.
"""

def sort_by_priority(fruits, priorities):
    # Combine the two lists into a list of tuples
    priority_fruits = list(zip(priorities, fruits))
    
    # Sort the list of tuples, first by priority, then alphabetically
    priority_fruits.sort(key = lambda x: (x[0], x[1]))
    
    # Extract the fruit names from the sorted list as a string
    sorted_fruits = ", ".join([fruit for _, fruit in priority_fruits])
    
    return sorted_fruits