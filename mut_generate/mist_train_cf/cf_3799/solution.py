"""
QUESTION:
Write a function `fill_dictionary(n)` that takes an integer `n` as input and returns a dictionary where the keys are numbers from 1 to `n` and the values are the squares of the corresponding keys. The function should use a recursive helper function `calculate_square(n)` to calculate the squares using the formula `(n^2) = (n-1)^2 + 2*(n-1) + 1`. The function should handle cases where `n` is less than or equal to 0 or not an integer by returning an empty dictionary.
"""

def fill_dictionary(n):
    def calculate_square(n):
        if n == 1:
            return 1
        else:
            return calculate_square(n-1) + 2*(n-1) + 1

    if n <= 0 or not isinstance(n, int):
        return {}

    dictionary = {}
    for i in range(1, n+1):
        dictionary[i] = calculate_square(i)
    return dictionary