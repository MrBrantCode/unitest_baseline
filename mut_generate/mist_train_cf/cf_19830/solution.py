"""
QUESTION:
Write a function `find_sum(numbers, N, M, K)` that takes in an array of N positive integers `numbers`, and three positive integers `N`, `M`, and `K`. The function should calculate the sum of the numbers in the array, add `M` to the sum, and return the result if it is greater than `K`. If the sum is not greater than `K`, the function should increment `M` by 1 and repeat the process until the sum is greater than `K`.
"""

def entrance(numbers, N, M, K):
    total_sum = 0
    for num in numbers:
        total_sum += num
    total_sum += M

    if total_sum > K:
        return total_sum
    else:
        M += 1
        return entrance(numbers, N, M, K)