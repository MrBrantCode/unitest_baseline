"""
QUESTION:
Create a function named `sort_array` that takes an array of dictionaries as input, where each dictionary has 'name' (string), 'age' (integer), and 'salary' (float) keys. Sort the array in descending order, prioritizing 'age' first, then 'salary', and finally 'name'. The function should return the sorted array.
"""

def sort_array(arr):
    arr.sort(key=lambda x: (x['age'], x['salary'], x['name']), reverse=True)
    return arr