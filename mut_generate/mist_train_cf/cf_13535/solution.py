"""
QUESTION:
Write a function called `sum_of_even_numbers` that takes a list of numbers as input and returns the sum of all even numbers in the list. The function must have a time complexity of O(n), where n is the length of the list, and a space complexity of O(1), meaning it cannot use any additional data structures to store intermediate results.
"""

def sum_of_even_numbers(arr):
    sum = 0
    for num in arr:
        if num % 2 == 0:
            sum += num
    return sum