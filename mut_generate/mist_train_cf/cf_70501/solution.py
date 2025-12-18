"""
QUESTION:
Write a function `unique_in_order` that takes an array of integers as input and returns a sequence that retains the first occurrence of each integer, discards any repeated occurrences, and maintains the original order. The function should not use any built-in functions or additional libraries, and it should be able to handle arrays containing negative values and zeros.
"""

def unique_in_order(objects):
    result = []
    seen = set()

    for number in objects:
        if number not in seen:
            result.append(number)
            seen.add(number)
            
    return result