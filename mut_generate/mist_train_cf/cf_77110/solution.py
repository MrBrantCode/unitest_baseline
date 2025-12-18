"""
QUESTION:
Write a function named `count_nums_plus` that accepts a list of integers and strings, and returns the quantity of elements whose absolute value exceeds zero and is divisible by either 4 or 5. The function should convert all string entities into integers and discard any entities that are not convertible.
"""

def count_nums_plus(arr):
    count = 0
    for element in arr:
        try:
            num = int(element)
            if num < 0:
                num *= -1
            if num > 0 and (num % 4 == 0 or num % 5 == 0):
                count += 1
        except ValueError:
            continue
    return count