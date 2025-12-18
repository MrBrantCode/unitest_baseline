"""
QUESTION:
Write a function named `square_odd_numbers` that takes a list of integers as input, calculates the squares of the unique odd numbers, and returns them as a new list. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the input list.
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