"""
QUESTION:
Write a function called `repeat_elements` that takes an array of strings `alphabet` as input and returns a new array where each element from `alphabet` is repeated a number of times equal to its length. Do not use built-in methods or functions for repetition. Handle edge cases such as empty strings in the array and arrays with multiple elements of the same length. Optimize the code for performance and handle any potential errors or exceptions that may occur during execution.
"""

def repeat_elements(alphabet):
    repeated_elements = []
    
    for element in alphabet:
        length = len(element)
        
        if length == 0:
            continue
        
        repeated_element = element * length
        repeated_elements.append(repeated_element)
            
    return repeated_elements