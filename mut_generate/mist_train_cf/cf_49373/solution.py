"""
QUESTION:
Write a function `plusOne(digits)` that takes a non-empty array of decimal digits as input and returns the array with the digits incremented by one, handling any carry that may occur when a digit is 9. The input array represents a non-negative integer where the most significant digit is at the head of the list and each element in the array contains a single digit. Assume the integer does not contain any leading zero, except the number 0 itself. The function should return an array of length 1 <= n <= 1000, where 0 <= digits[i] <= 9.
"""

def plusOne(digits):
    index = len(digits) - 1
    while index >= 0:
        if digits[index] == 9:
            digits[index] = 0
            index -= 1
        else:
            digits[index] += 1
            return digits
    return [1] + digits