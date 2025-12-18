"""
QUESTION:
Write a function `find_max_unique` that takes a list of integers as input and returns a new list containing the maximum value of each unique number in the input list. The function should have a time complexity of O(n), where n is the length of the input list, and it should not use any built-in Python functions or libraries for finding the maximum value of a list or removing duplicates. It should also handle negative integers and not use any additional data structures such as dictionaries or sets to track unique numbers.
"""

def find_max_unique(numbers):
    max_values = []
    seen_numbers = set()
    for num in numbers:
        if num not in seen_numbers:
            seen_numbers.add(num)
            max_value = num
            for i in range(len(numbers)):
                if numbers[i] == num and numbers[i] > max_value:
                    max_value = numbers[i]
            max_values.append(max_value)
    return max_values