"""
QUESTION:
Given a list of N positive integers, a positive integer M, and a positive integer K, write a function `find_sum` that returns the sum of the numbers in the list plus M if the sum is greater than K. If the sum is not greater than K, increase M by 1 and repeat the process.
"""

def find_sum(numbers, N, M, K):
    total_sum = 0
    for num in numbers:
        total_sum += num
    total_sum += M

    if total_sum > K:
        return total_sum
    else:
        M += 1
        return find_sum(numbers, N, M, K)