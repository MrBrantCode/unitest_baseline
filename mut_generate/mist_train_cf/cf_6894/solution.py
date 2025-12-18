"""
QUESTION:
Write a function named `calculate_sum` that calculates the sum of all positive even numbers greater than 5 and less than or equal to 10^9 in a given array, and if the sum is divisible by 7, subtract the smallest positive even number from the sum until it is no longer divisible by 7. The array may contain duplicates, negative numbers, and numbers greater than 10^9.
"""

def calculate_sum(arr):
    sum = 0
    smallest_even = float('inf')
    for num in arr:
        if num > 5 and num <= 10**9 and num % 2 == 0:
            sum += num
            smallest_even = min(smallest_even, num)
    while sum % 7 == 0 and smallest_even != float('inf'):
        sum -= smallest_even
    return sum