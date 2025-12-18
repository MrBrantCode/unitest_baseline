"""
QUESTION:
Implement a function called `bubble_sort` that sorts a list of numbers in ascending order (from least to greatest) using nested if statements within a loop structure, without relying on built-in sorting functions. The input list can contain both positive and negative integers.
"""

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    return numbers