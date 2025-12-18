"""
QUESTION:
Create a function `process_number(num)` that takes an integer `num` as input. The function should handle potential exceptions when converting `num` to an integer and check if `num` is indeed an integer. It should skip processing if `num` is an odd number between 5 and 10 (exclusive). Implement a switch-like statement using a dictionary to handle different cases of `num` and provide a default case if no match is found. The function should use integers, booleans, and conditional operators.
"""

def process_number(num):
    try:
        num = int(num) # try to convert num to integer, this will fail if num is not a number
    except ValueError:
        print(f'Error: {num} is not a number')
        return
    if not isinstance(num, int): # double check if num is integer
        print(f'Error: {num} is not an integer number')
        return
    if num > 5 and num < 10 and num % 2 != 0:
        return # skip odd numbers between 5 and 10
    switch = {
        1 : lambda : print(f'{num} is 1'),
        2 : lambda : print(f'{num} is 2'),
        # Extend the cases here as needed, or provide a default case
    }
    try:
        switch.get(num, lambda : print(f"{num} doesn't corresponds to any case"))()
    except Exception as e:
        print(f"An error occurred: {e}")