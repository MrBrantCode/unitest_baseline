"""
QUESTION:
Write a function named `sum_of_numbers` that calculates the sum of the first N natural numbers. The function should take one integer parameter `N` and return the sum as an integer. The time complexity of the function should be O(N) and the space complexity should be O(1).
"""

def sum_of_numbers(N):
    total = 0
    for i in range(1, N+1):
        total += i
    return total