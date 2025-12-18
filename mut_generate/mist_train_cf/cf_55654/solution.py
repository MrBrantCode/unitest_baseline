"""
QUESTION:
Write a function `short_circuit_sum` that takes a list of numbers and a target sum. It should return True if the cumulative sum of the numbers exceeds the target sum and False otherwise. The function should stop iterating over the list as soon as the cumulative sum exceeds the target sum.
"""

def short_circuit_sum(numbers, target_sum):
    cumulative_sum = 0
    for num in numbers:
        cumulative_sum += num
        if cumulative_sum > target_sum:
            return True
    return False