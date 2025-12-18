"""
QUESTION:
Write a function named `find_second_smallest_prime` that finds the second smallest prime number in a given list of integers. The function should not use any built-in sorting functions or libraries and should have a time complexity of O(n). The function should return `None` if there is no second smallest prime number in the list. The input list can contain duplicate numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_second_smallest_prime(lst):
    smallest = float('inf')
    second_smallest = float('inf')
    for num in lst:
        if is_prime(num):
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest and num != smallest:
                second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest