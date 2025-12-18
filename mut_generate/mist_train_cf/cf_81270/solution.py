"""
QUESTION:
Write a function named `five_nine_sixteen` that takes an integer `n` as input and returns the count of integers smaller than `n` that contain the digit 5 and are divisible by either 9, 16, or both. The function should handle cases where `n` or the factors for division are negative.
"""

def five_nine_sixteen(n: int) -> int:
    nums = [i for i in range(n) if '5' in str(abs(i)) and (abs(i) % 9 == 0 or abs(i) % 16 == 0) ]
    return len(nums)