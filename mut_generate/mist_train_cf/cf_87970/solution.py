"""
QUESTION:
Create a function named `square_odd_numbers` that takes a list of integers as input and returns a new list containing the squares of each unique odd element in the input list. The function should exclude even numbers and duplicates, and correctly handle negative input values. The time complexity should be O(n) and the space complexity should be O(n), where n is the number of elements in the input list.
"""

def square_odd_numbers(input_list):
    squared_list = []
    seen = set()  # To keep track of unique odd numbers
    
    for num in input_list:
        if num % 2 != 0:  # Only consider odd numbers
            if num not in seen:  # Exclude duplicates
                squared_list.append(num ** 2)
                seen.add(num)
    
    return squared_list