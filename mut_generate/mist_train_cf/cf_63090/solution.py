"""
QUESTION:
Write a function called `reverse_strings` that takes an array of strings as input and returns the array with the sequence of elements reversed and the individual strings within the array reversed. Do not use any built-in reverse methods.
"""

def reverse_strings(input_list):
    # Reverse the order of the list
    input_list = input_list[::-1]
    
    # Reverse each string in the list
    for i in range(len(input_list)):
        input_list[i] = input_list[i][::-1]
    
    return input_list