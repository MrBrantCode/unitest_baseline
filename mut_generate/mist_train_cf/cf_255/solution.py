"""
QUESTION:
Write a function `check_sum_and_product(arr, target, threshold)` that takes an array of integers, a target value, and a threshold value as input. The function should return True if there exists a pair of numbers in the array whose sum equals the target value and whose product is greater than the threshold, and False otherwise.
"""

def check_sum_and_product(arr, target, threshold):
    seen_numbers = set()
    for num in arr:
        if target - num in seen_numbers:
            product = num * (target - num)
            if product > threshold:
                return True
        seen_numbers.add(num)
    return False