"""
QUESTION:
Create a function named `triangle_sum` that calculates the sum of the first n natural numbers and returns the sum along with the number of terms in the series. The function should only use a loop structure and not rely on built-in mathematical functions or libraries.
"""

def triangle_sum(n):
    total_sum = 0
    num_terms = 0
    for i in range(1, n+1):
        total_sum += i
        num_terms += 1
    return total_sum, num_terms