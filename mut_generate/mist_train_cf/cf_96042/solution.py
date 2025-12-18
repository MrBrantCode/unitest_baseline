"""
QUESTION:
Create a function called `contains_in_order` that takes two integer arrays as parameters. The function should return True if the first array contains all the elements in the second array in the same order, without any other elements in between, and False otherwise. You are not allowed to use any built-in functions or methods that directly solve this problem, such as `array.index()` or `array.count()`.
"""

def contains_in_order(array1, array2):
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] == array2[j]:
            j += 1
        i += 1
    return j == len(array2)