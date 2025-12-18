"""
QUESTION:
Design a function named `longest_uninterrupted_chain` that takes a string of characters as input and returns a tuple containing the character with the longest uninterrupted chain and the length of that chain. If there are multiple chains of the same length, the function should return the first one encountered in the string.
"""

def longest_uninterrupted_chain(my_string):
    max_chain = 0
    current_chain = 1
    max_char = ''
    
    for i in range(1, len(my_string)):
        if my_string[i] == my_string[i-1]:
            current_chain += 1
        else:
            if current_chain > max_chain:
                max_chain = current_chain
                max_char = my_string[i-1]
            current_chain = 1
    
    if current_chain > max_chain:
        max_chain = current_chain
        max_char = my_string[-1]
    return max_char, max_chain