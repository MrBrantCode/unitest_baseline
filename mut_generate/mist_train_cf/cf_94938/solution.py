"""
QUESTION:
Write a function named `remove_even_duplicates` that takes an array of numbers as input, removes even numbers and duplicates from the array, and returns the resulting array. The function should use recursion, have a time complexity of O(n^2), and work for arrays of any length containing both positive and negative numbers.
"""

def remove_even_duplicates(arr):
    # Base case: if the array is empty, return an empty array
    if not arr:
        return []
    
    # Recursive case:
    # Get the first element of the array
    first = arr[0]
    
    # If the first element is even, remove it from the array and recursively call the function with the remaining elements
    if first % 2 == 0:
        return remove_even_duplicates(arr[1:])
    
    # If the first element is odd, remove all occurrences of it from the array and recursively call the function with the remaining elements
    return [first] + remove_even_duplicates([x for x in arr[1:] if x != first])