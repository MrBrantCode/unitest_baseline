"""
QUESTION:
Write a function called `sum_odd_numbers` that takes an integer `n` as input and returns the sum of all odd numbers from 0 to `n` using a combination of while loop and recursion. The function should have a default parameter `current` initialized to 0 and `sum` initialized to 0. The function should be able to handle large inputs, but note that the recursive approach may have performance limitations due to the maximum recursion depth.
"""

def sum_odd_numbers(n, current=0, sum=0):
    while current <= n:
        if current % 2 != 0:
            sum += current
        current += 1
        return sum_odd_numbers(n, current, sum)
    return sum