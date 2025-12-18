"""
QUESTION:
Write a function `max_sequence_sum(numbers, k)` that takes a list of integers `numbers` and an integer `k` as input, and returns the maximum cumulative sum of `k` consecutive integers in the list. The function should have a time complexity of less than O(n^2).
"""

def max_sequence_sum(numbers, k):
    # Calculate the initial sum
    sum_k_numbers = sum(numbers[:k])
    max_sum = sum_k_numbers
    for i in range(k, len(numbers)):
        # Subtract the left most number and add the new rightmost number
        sum_k_numbers = sum_k_numbers - numbers[i - k] + numbers[i]
        max_sum = max(max_sum, sum_k_numbers)
    return max_sum