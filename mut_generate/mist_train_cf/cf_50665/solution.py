"""
QUESTION:
Create a function `find_sum_pair(numbers, target)` that takes a list of numbers and a target number as input, and returns a pair of numbers in the list that sum up to the target number. If no such pair exists, the function should return `None`. The function should be able to handle edge cases, such as multiple pairs with the same sum, and should be efficient for large input lists.
"""

def find_sum_pair(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])
    return None