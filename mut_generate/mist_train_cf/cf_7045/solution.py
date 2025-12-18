"""
QUESTION:
Create a function named `create_random_string` that takes an input string of lowercase alphabets as a parameter. The function should return a new string of length 10 consisting of characters from the input string. The function should not use any built-in random functions or libraries and should have a time complexity of O(n).
"""

def create_random_string(input_string):
    new_string = ""
    index = 0
    length = len(input_string)
    
    while len(new_string) < 10:
        index = (index + 1) % length
        new_string += input_string[index]
    
    return new_string