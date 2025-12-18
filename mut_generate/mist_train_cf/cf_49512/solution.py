"""
QUESTION:
Write a function called `combinations` that calculates the number of combinations of reading two books from each category. The function should take two parameters: `n`, the number of books in a category, and `r`, the number of books to be chosen (which is always 2 in this case). Then use this function to calculate the total number of combinations for four categories with 15, 12, 5, and 21 books respectively. The total number of combinations should be the product of the combinations for each category.
"""

import math

def combinations(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))