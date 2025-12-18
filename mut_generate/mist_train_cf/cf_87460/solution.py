"""
QUESTION:
Create a function named `find_two_largest` that takes a list of integers as input and returns the two largest numbers in the list. The function should have a time complexity of O(n), not use any built-in sorting or max/min functions, and not use any additional data structures to store intermediate values. The function should iterate through the list only once, not modify the original list, and handle cases where the input list contains negative numbers, duplicate numbers, or has a length less than 2.
"""

def find_two_largest(numbers):
    if len(numbers) < 2:
        return "Error: Input list must contain at least two numbers."
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return (largest, None)
    else:
        return (largest, second_largest)