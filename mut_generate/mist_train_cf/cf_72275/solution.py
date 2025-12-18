"""
QUESTION:
Create a function called `apply_to_each` that takes another function and a list of numbers as parameters. The function should apply the given function to each number in the list, handling cases where the input list contains non-numeric values by printing an error message and skipping them. The function should return a list of the results. The given function can be a lambda expression that calculates the square of a number.
"""

def apply_to_each(function, lst):
    result = []
    for x in lst:
        try:
            result.append(function(x))
        except (TypeError, ValueError) as e:
            print(f"Error: non-numeric value {x} in list. Skipping...")
    return result