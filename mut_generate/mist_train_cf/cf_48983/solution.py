"""
QUESTION:
Write a Python function named `lowest_even_numbers` that takes a list of integers as input and returns the three lowest even numbers in the list. If the list does not contain up to three even numbers, the function should return a message indicating that. The function should be efficient and handle edge cases.
"""

def lowest_even_numbers(data_set):
    even_numbers = [num for num in data_set if num % 2 == 0]
    
    if len(even_numbers) < 3:
        return "The list does not contain up to three even numbers."
        
    even_numbers.sort()
    
    return even_numbers[:3]