"""
QUESTION:
Write a program that includes two functions: `reverse_list` and `sort_numbers`. The `reverse_list` function should reverse a given list of numbers without using any built-in methods or additional data structures. The `sort_numbers` function should sort a list of numbers in ascending order without using any built-in sorting methods. Implement these functions to handle a list of integers.
"""

def entrance(numbers):
    def reverse_list(numbers):
        start = 0
        end = len(numbers) - 1

        while start < end:
            numbers[start], numbers[end] = numbers[end], numbers[start]
            start += 1
            end -= 1
        return numbers

    def sort_numbers(numbers):
        n = len(numbers)

        for i in range(n):
            for j in range(n-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        return numbers

    reversed_numbers = reverse_list(numbers)
    return sort_numbers(reversed_numbers)