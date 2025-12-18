"""
QUESTION:
Write a function named `custom_sort` that takes a dictionary as input, converts it into a list of key-value pairs, sorts the list in descending order based on the keys without using any built-in sorting functions, and returns the sorted list.
"""

def custom_sort(dictionary):
    # Convert the dictionary into a list of tuples
    items = list(dictionary.items())
    
    # Custom sorting algorithm
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i][0] < items[j][0]:
                items[i], items[j] = items[j], items[i]
    
    return items