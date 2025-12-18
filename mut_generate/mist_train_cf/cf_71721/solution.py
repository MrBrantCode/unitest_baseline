"""
QUESTION:
Write a function `main` that takes two parameters, an integer `x` and a list of integers `y`, and returns a result calculated as follows: it first calculates the average of numbers in `y` that are greater than or equal to `x`, multiplies this average by 5, adds `x` to the product, and then adds 5 to the sum if `x` is in `y` or subtracts 2 if `x` is not in `y`. If no elements in `y` are greater than or equal to `x`, the function should handle this case without crashing and return a corresponding result.
"""

def main(x, y):
    count = 0
    total = 0
    for i in y:
        if i >= x:
            count += 1
            total += i
    
    if count == 0:
        print("No elements in the list are greater than or equal to x.")
        return None

    average = total / count
    result = x + 5*average
    if x in y:
        result += 5
    else:
        result -= 2
    return result