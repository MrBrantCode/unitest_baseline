"""
QUESTION:
Write a function `prod_signs(arr)` that takes an array of non-zero integers of length 1-100, removes duplicates, and returns the sum of the magnitudes of distinct integers multiplied by the product of all signs of each distinct number. If the array contains zero or is empty, or if its length exceeds 100, return None.
"""

def prod_signs(arr):
    if 0 in arr or len(arr) > 100 or len(arr) == 0:
        return None
    else:
        arr = list(set(arr))
        signs = [1 if x > 0 else -1 for x in arr]
        magnitudes = [abs(x) for x in arr]
        return sum([x * y for x, y in zip(signs, magnitudes)])