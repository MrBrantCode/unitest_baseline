"""
QUESTION:
Write a function `separate_string` that takes a string of alphanumeric characters as input, separates it into left and right parts, and returns them as a tuple of two strings. The left part should contain only digits sorted in non-decreasing order, and the right part should contain only lowercase letters. If there are no lowercase letters in the string, the right part should be an empty string. The function should have a time complexity of O(n log n) due to the sorting requirement, and it should be implemented using a single loop and without using any built-in sorting functions.
"""

def separate_string(s):
    left = ""
    right = ""
    
    for char in s:
        if char.isdigit():
            left += char
        elif char.islower():
            right += char
    
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        
        return quicksort(lesser) + [pivot] + quicksort(greater)
    
    left = quicksort(left)
    
    if right == "":
        return "".join(left), ""
    
    return "".join(left), right