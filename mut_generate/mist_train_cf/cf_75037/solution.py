"""
QUESTION:
Design a function called `common` that takes two lists of integers as input and returns a list of unique elements common to both lists in ascending order. The function should handle negative numbers and not use any built-in Python functions (except for loops and if-else conditions), built-in list features, or collection modules. Implement a sorting algorithm to achieve the sorted output.
"""

# Sorting algorithm
def my_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# Function to find common elements
def common(list1, list2):
    """
    Returns a sorted list of unique elements common to two lists. Also handles negative numbers.
    """
    output = []
    for i in list1:
        if i in list2 and i not in output:
            output.append(i)
    return my_sort(output)