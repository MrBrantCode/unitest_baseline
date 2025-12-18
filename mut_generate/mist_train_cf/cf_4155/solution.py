"""
QUESTION:
Write a function `get_sorted_odd_numbers` that takes a list of integers as input and returns a list of odd numbers in descending order. The function should achieve this in a single loop and without using any built-in sorting functions or libraries. The resulting time complexity should be O(n).
"""

def get_sorted_odd_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    for i in range(len(odd_numbers)):
        for j in range(i + 1, len(odd_numbers)):
            if odd_numbers[i] < odd_numbers[j]:
                odd_numbers[i], odd_numbers[j] = odd_numbers[j], odd_numbers[i]
    return odd_numbers