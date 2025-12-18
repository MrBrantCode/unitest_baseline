"""
QUESTION:
Create a function called `sum_even_divisible_by_three` that takes a list of integers as input and returns the sum of all even elements in the list that are divisible by 3. If the list is empty or contains only odd elements, the function should return -1.
"""

def sum_even_divisible_by_three(numbers):
    # Check if the list is empty or contains only odd elements
    if len(numbers) == 0 or all(num % 2 != 0 for num in numbers):
        return -1
    
    # Use list comprehension to filter even numbers divisible by 3
    filtered_numbers = [num for num in numbers if num % 2 == 0 and num % 3 == 0]
    
    # Return the sum of the filtered numbers
    return sum(filtered_numbers)