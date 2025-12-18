"""
QUESTION:
Create a function named `multiply_sort` that takes an array of positive integers as input and returns a new array. The returned array should contain each element from the input array multiplied by 3, sorted in descending order, with no duplicates, and only include numbers that are divisible by 2.
"""

def multiply_sort(arr):
    unique_elements = set(arr)
    result = []
    
    for num in unique_elements:
        if num % 2 == 0:
            result.append(num * 3)
    
    return sorted(result, reverse=True)