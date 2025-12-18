"""
QUESTION:
Write a function called `find_fibonacci_index` that takes an integer `digit_length` as input and returns the position of the first term in the Fibonacci sequence that reaches a length of `digit_length` digits. The function should handle integer numbers of arbitrary size.
"""

def find_fibonacci_index(digit_length):
    F1, F2 = 1, 1
    index = 2 # The first two Fibonacci numbers are already provided
    while True:
        F1, F2 = F2, F1 + F2 # Recurrence relation
        index += 1 # Increment the index for each new Fibonacci number
        if len(str(F2)) >= digit_length: # Check the length of the new number
            return index