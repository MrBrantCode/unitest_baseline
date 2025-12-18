"""
QUESTION:
Create a function that takes a number and finds the factors of it, listing them in **descending** order in an **array**.

If the parameter is not an integer or less than 1, return `-1`. In C# return an empty array.

For Example:
`factors(54)` should return `[54, 27, 18, 9, 6, 3, 2, 1]`
"""

def get_factors(number: int) -> list[int] | int:
    if not isinstance(number, int) or number < 1:
        return -1
    return [i for i in range(number, 0, -1) if number % i == 0]