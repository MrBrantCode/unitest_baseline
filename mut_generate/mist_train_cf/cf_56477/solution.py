"""
QUESTION:
Write a function `numeric_signs(array)` that takes an array of non-zero integers and floating-point numbers, calculates the sum of distinct numeric magnitudes multiplied by their respective signs, and returns the result. If the array contains no numeric elements or all zero elements, return `None`. The function should ignore null and repeated elements.
"""

def numeric_signs(array):
    if not array or all(val == 0 for val in array):
        return None

    seen = set()
    total = 0.0
    for num in array:
        if num == 0 or num is None:
            continue
        abs_num = abs(num)
        if abs_num not in seen:
            seen.add(abs_num)
            total += abs_num * (num/abs_num)
    return total