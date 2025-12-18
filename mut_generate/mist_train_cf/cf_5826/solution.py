"""
QUESTION:
Write a function `repeat_elements(alphabet)` that takes an array of strings as input and returns a new array where each element in the input array is repeated a number of times equal to its length. The function should not use any built-in methods or functions for repetition. It must handle edge cases such as empty strings in the array and arrays with multiple elements of the same length, and be optimized for performance.
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