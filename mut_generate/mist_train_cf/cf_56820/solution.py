"""
QUESTION:
Write a recursive function `count_divisible_by_k(arr, k)` that counts the total number of elements in a multidimensional array `arr` that are divisible by a given integer `k`. If `k` is 0, the function should return an error message. The function should ignore non-integer elements in the array.
"""

def count_divisible_by_k(arr, k):
    if k == 0:
        return "Error: Division by zero is undefined"

    count = 0
    for i in arr:
        if isinstance(i, list):
            count += count_divisible_by_k(i, k)
        elif isinstance(i, (int, float)):
            if i % k == 0:
                count += 1
                
    return count