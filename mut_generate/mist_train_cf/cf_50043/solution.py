"""
QUESTION:
Develop a function named `sort_func` that sorts an array of alphanumeric strings in ascending order. Each string contains a numerical value followed by a single character. The sorting should prioritize the numerical value; if two strings have the same numerical value, they should be sorted alphabetically by the character. The function should be efficient for large datasets.
"""

def sort_func(arr):
    def sorter(item):
        num, alpha = item[:-1], item[-1] 
        return int(num), alpha  

    arr.sort(key=sorter)
    return arr