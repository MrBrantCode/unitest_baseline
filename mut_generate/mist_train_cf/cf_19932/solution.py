"""
QUESTION:
Create a function named `consolidate_fruits` that takes an array of tuples as input, where each tuple contains a fruit name and its count. The function should return a dictionary with the fruit names as keys and their counts as values, but only include fruits with a count greater than 1. The fruits in the dictionary should be sorted in descending order based on their count. You are not allowed to use any built-in sorting functions or libraries for this task.
"""

def consolidate_fruits(fruits):
    fruit_dict = {}
    
    for fruit, count in fruits:
        if count > 1:
            fruit_dict[fruit] = count
    
    sorted_fruits = sorted(fruit_dict.items(), key=lambda x: x[1], reverse=True)
    
    return dict(sorted_fruits)