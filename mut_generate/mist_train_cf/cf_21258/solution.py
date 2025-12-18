"""
QUESTION:
Create a function `find_top_k_biggest_numbers(numbers, k)` that takes a list of integers `numbers` and a positive integer `k` as input, and returns the top `k` biggest numbers from the list in descending order, handling duplicate numbers and ensuring the correct number of distinct top `k` biggest numbers are returned.
"""

def find_top_k_biggest_numbers(numbers, k):
    distinct_numbers = list(set(numbers))
    sorted_numbers = sorted(distinct_numbers, reverse=True)
    top_k_numbers = sorted_numbers[:k]
    return top_k_numbers