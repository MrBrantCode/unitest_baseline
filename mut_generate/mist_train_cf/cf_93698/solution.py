"""
QUESTION:
Write a function named `sum_even_divisible_by_three` that takes a list of integers as input and returns the sum of all the even numbers in the list that are divisible by 3. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the list. The input list may have a maximum length of 100 elements, and it may contain duplicate elements. The function must not use any built-in functions for finding the sum.
"""

def sum_even_divisible_by_three(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0 and num % 3 == 0:
            total += num
    return total