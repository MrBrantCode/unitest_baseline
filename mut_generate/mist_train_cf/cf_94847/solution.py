"""
QUESTION:
Create a function `count_pairs_divisible_by_three` that takes a list of integers as input and returns the count of pairs whose sum is divisible by 3. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def count_pairs_divisible_by_three(lst):
    # Initialize counters
    count = 0
    remainder_count = [0] * 3

    # Count the remainder of each element when divided by 3
    for num in lst:
        remainder = num % 3
        remainder_count[remainder] += 1

    # Count pairs whose sum is divisible by 3
    count += (remainder_count[0] * (remainder_count[0] - 1)) // 2  # Count pairs with remainder 0
    count += remainder_count[1] * remainder_count[2]  # Count pairs with remainder 1 and 2

    return count