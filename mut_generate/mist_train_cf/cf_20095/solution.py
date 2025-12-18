"""
QUESTION:
Create a function `build_even_dictionary` that takes a list of integers as input and returns a dictionary containing all even numbers greater than 5. The dictionary should have the even numbers as keys and their respective counts in the input list as values.
"""

def build_even_dictionary(numbers):
    even_dict = {}
    
    for num in numbers:
        if num > 5 and num % 2 == 0:
            if num not in even_dict:
                even_dict[num] = 1
            else:
                even_dict[num] += 1
    
    return even_dict