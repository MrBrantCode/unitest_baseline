"""
QUESTION:
Write a function named `generate_next_line` that takes a list of integers representing the current line of Pascal's Triangle and returns a list of integers representing the next line. The next line should be generated based on the rule that each element is the sum of the two elements directly above it in the previous line. The function should assume that the input list is valid and will not contain any errors.
"""

def generate_next_line(parent_line):
    next_line = [1]  
    for i in range(len(parent_line) - 1):
        next_line.append(parent_line[i] + parent_line[i+1])  
    next_line.append(1)  
    return next_line