"""
QUESTION:
Write a function `calculate_even_sum` that calculates the sum of the even numbers in an array of positive integers with a length of at least 10. The function should use a single loop to iterate through the array, have a time complexity of O(n), and a space complexity of O(1).
"""

def calculate_even_sum(arr):
    even_sum = 0
    for num in arr:
        if num % 2 == 0:
            even_sum += num
    return even_sum