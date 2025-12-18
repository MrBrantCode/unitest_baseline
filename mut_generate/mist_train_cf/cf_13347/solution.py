"""
QUESTION:
Create a function named `generate_even_array` that takes an integer `n` as input. The function should return an array of length `n` where the first two elements are 0 and 2, and each subsequent element is the sum of the previous two elements. If `n` is less than 2, the function should return an array containing only 0.
"""

def generate_even_array(n):
    if n < 2:
        return [0]
    
    arr = [0, 2]  # Initialize the array with the first two even numbers
    
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])  # Add the sum of the previous two even numbers
        
    return arr