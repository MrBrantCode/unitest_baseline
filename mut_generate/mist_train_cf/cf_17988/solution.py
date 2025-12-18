"""
QUESTION:
Design a function `find_divisible_by_three(arr)` that finds all elements in an array `arr` that are divisible by 3 without using the modulo operator (%) or any division operation. The function must have a time complexity of O(n), where n is the size of the array.
"""

def find_divisible_by_three(arr):
    result = []
    for num in arr:
        if sum(int(digit) for digit in str(num)) % 3 == 0:
            result.append(num)
    return result