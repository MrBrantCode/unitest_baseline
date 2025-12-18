"""
QUESTION:
Function `lastNumberRemaining` is required to find the last number that remains after applying a series of operations on a list of integers in the range `[1, n]`, sorted in strictly increasing order. The operations involve replacing every other number with the sum of the previous or next two numbers, alternating from left to right and right to left, and rotating the remaining elements after each replacement round. The rotation steps are equal to the number of elements replaced in that round and are performed to the right for rounds starting from the left and to the left for rounds starting from the right. The function should take an integer `n` as input, where `1 <= n <= 10^9`, and return the last remaining number.
"""

def lastNumberRemaining(n: int) -> int:
    if n == 1:
        return 1
    if n % 2 == 1:
        return 2 * lastNumberRemaining(n - 1)
    else:
        return 2 * lastNumberRemaining(n // 2)