"""
QUESTION:
Create a function called `square_integers` that accepts an array of integers. The function should return an array where each element is the square of its corresponding element in the input array, with negative numbers squared as their absolute values. If an absolute value appears more than once in the input array, replace its subsequent occurrences with zeros, while maintaining their original positions.
"""

def square_integers(arr):
    results = []
    seen = set()
    for i, num in enumerate(arr):
        abs_val = abs(num)
        if abs_val in seen:
            results.append(0)
        else:
            results.append(abs_val**2)
            seen.add(abs_val)
    return results