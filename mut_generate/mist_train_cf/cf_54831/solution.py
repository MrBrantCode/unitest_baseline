"""
QUESTION:
Create a function called `get_even_numbers` that takes a list of numbers as input and returns a new list containing only the even numbers. The function should ignore non-integer values in the input list and handle exceptions without crashing. The input list may contain non-numeric types.
"""

def entrance(numbers):
    even_numbers = []  

    for number in numbers:  
        if type(number) is int:  
            if number % 2 == 0:  
                even_numbers.append(number)  
    return even_numbers  