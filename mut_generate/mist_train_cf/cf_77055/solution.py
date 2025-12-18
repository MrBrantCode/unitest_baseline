"""
QUESTION:
Create a function called `separate_even_odd_numbers` that uses a loop structure to traverse a given list of integers and separate the numbers into two lists: one for even numbers and one for odd numbers. The function should return both lists.
"""

def separate_even_odd_numbers(lst):
    even_numbers = []
    odd_numbers = []
    
    for i in lst:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    
    return even_numbers, odd_numbers