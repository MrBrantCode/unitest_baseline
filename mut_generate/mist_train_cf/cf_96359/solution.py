"""
QUESTION:
Write a function `foo_bar_array(n)` that generates an array of numbers from 1 to `n` using list comprehension and filters the numbers that are divisible by both 2 and 3 using a lambda function. The function should return the filtered array in reverse order.
"""

def foo_bar_array(n):
    # Generate fooBarArray using list comprehension
    fooBarArray = [num for num in range(1, n + 1) if num % 2 == 0 and num % 3 == 0]
    
    # Filter fooBarArray using a lambda function
    filteredArray = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, fooBarArray))
    
    # Return the filtered fooBarArray in reverse order
    return filteredArray[::-1]