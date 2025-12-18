"""
QUESTION:
Write a function called `calculate_sum` that takes a set of positive numbers as input and returns the sum of all numbers in the set, excluding any numbers that are divisible by 3. The function should handle empty sets and have a time complexity of O(n), where n is the size of the set.
"""

def calculate_sum(my_set):
    sum = 0
    for number in my_set:
        if number % 3 == 0:
            continue
        sum += number
    return sum