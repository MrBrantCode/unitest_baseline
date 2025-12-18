"""
QUESTION:
Create a function called `get_even_set` that takes a list of integers as input and returns a set of only the even numbers from the list. The function should not use any built-in Python functions or methods, except for basic operations such as loops and conditional statements.
"""

def get_even_set(numbers):
    even_set = set()  
    for num in numbers:  
        if num % 2 == 0:  
            even_set.add(num)  
    return even_set 