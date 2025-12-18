"""
QUESTION:
Create a function named `productExceptSelf` that takes an array of integers `nums` as input and returns an array where each element at index `i` is the product of all the numbers in the input array except the one at index `i`. The function should not use division.
"""

def productExceptSelf(nums):
    length = len(nums)

    # Initialize two empty arrays: L and R
    L, R, product = [0]*length, [0]*length, [0]*length

    # L[i] contains the product of all the numbers to the left of i
    L[0] = 1
    for i in range(1, length):
        L[i] = nums[i - 1] * L[i - 1]

    # R[i] contains the product of all the numbers to the right of i
    R[length - 1] = 1
    for i in reversed(range(length - 1)):
        R[i] = nums[i + 1] * R[i + 1]

    # For each index i in product, multiply L[i] and R[i]
    for i in range(length):
        product[i] = L[i] * R[i]

    return product