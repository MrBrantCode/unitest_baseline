"""
QUESTION:
Create a function `check_divisible(arr)` that takes an array of integers as input and returns `True` if the sum of any two integers in the array is divisible by 10, and `False` otherwise. The function should be computationally efficient.
"""

def check_divisible(arr):
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) % 10 == 0:
                return True
    return False