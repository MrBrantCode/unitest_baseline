"""
QUESTION:
Implement a recursive function `factorial(number, limit)` that calculates the factorial of a given `number` and the number of recursive calls needed to complete the calculation. The function should break the recursion if it exceeds the provided `limit` and return an error message if exceeded.
"""

def factorial(number, limit, counter=1):
    if counter > limit:
        return "Exceeded recursion limit."
    elif number == 0 or number == 1:
        return (1, counter)
    else:
        result, new_counter = factorial(number-1, limit, counter+1)
        return (number * result, new_counter)