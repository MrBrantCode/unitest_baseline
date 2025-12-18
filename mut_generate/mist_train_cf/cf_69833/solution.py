"""
QUESTION:
Create a function `process_numbers` that takes a list of numbers as input and applies a sequence of operations - subtraction, multiplication, and addition - to consecutive pairs of numbers in the list. The operations should follow the order: subtract the second number from the first, multiply the result by the third, add the result to the fourth, and continue this pattern for the length of the list. If the list is empty, return 0. The function should handle lists of varying lengths and avoid division by zero cases.
"""

def process_numbers(lst):
    if not lst:
        return 0
    num = lst[0]
    for i in range(1, len(lst)):
        if i % 3 == 1:
            num = lst[i] - num
        elif i % 3 == 2:
            num = num * lst[i]
        else:
            num = num + lst[i]
    return num