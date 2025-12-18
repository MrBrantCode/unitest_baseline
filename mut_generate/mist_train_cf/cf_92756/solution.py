"""
QUESTION:
Create a function `generate_even_array(n)` that generates an array of length `n` containing even numbers where each number (except the first two) is the sum of its two preceding numbers in the array. The array should start with 0, followed by 2. The function should return `[0]` for `n < 2`.
"""

def generate_even_array(n):
    if n < 2:
        return [0]
    
    arr = [0, 2]  # Initialize the array with the first two even numbers
    
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])  # Add the sum of the previous two even numbers
        
    return arr