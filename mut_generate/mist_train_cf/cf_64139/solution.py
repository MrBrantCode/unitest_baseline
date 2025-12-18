"""
QUESTION:
Construct a function `lucas_numbers(n)` that returns an array of all Lucas numbers less than or equal to a specified integer `n`, where Lucas numbers are defined as a sequence starting with 2 and 1, and each subsequent number is the sum of the previous two. Ensure the function is efficient and accurate. If `n` is less than 2, return an empty list.
"""

def lucas_numbers(n):
    if n < 2:
        return []
    lucas = [2, 1] 
    while True:
        new_number = lucas[-1] + lucas[-2] 
        if new_number > n: 
            break
        else:
            lucas.append(new_number) 
    return lucas