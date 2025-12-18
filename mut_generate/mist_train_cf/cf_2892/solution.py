"""
QUESTION:
Write a function `find_second_smallest_prime(lst)` that takes a list of integers `lst` and returns the second smallest prime number in the list. The function should not use any built-in sorting functions or libraries. The time complexity of the function should be O(n) and it should use constant space. If no second smallest prime number exists, the function should return `None`.
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