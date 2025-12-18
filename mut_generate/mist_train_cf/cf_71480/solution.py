"""
QUESTION:
Write a function `find_pairs` that takes four parameters: three arrays of integers (`array1`, `array2`, and `array3`) and a target integer `n`. The function should return all unique pairs of integers, one from `array1` and one from `array2`, whose sum equals `n` minus an integer from `array3`. The function should optimize for time efficiency to handle arrays of different lengths and potentially very large numbers.
"""

def find_pairs(array1, array2, array3, n):
    results = []
    seen = set()  # Set is used for O(1) lookup
    for i in array1:
        for j in array2:
            if n - i - j in array3 and (i, j, n-i-j) not in seen:
                seen.add((i, j, n-i-j))  # Add to seen set
                results.append((i, j, n-i-j))  # Add to results
    return results