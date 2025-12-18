"""
QUESTION:
Consider having a cow that gives a child every year from her fourth year of life on and all her subsequent children do the same.

After n years how many cows will you have?
Return null if n is not an integer.

Note: Assume all the cows are alive after n years.
"""

def calculate_cow_population(n):
    if not isinstance(n, int):
        return None
    if n < 3:
        return 1
    return calculate_cow_population(n - 1) + calculate_cow_population(n - 3)