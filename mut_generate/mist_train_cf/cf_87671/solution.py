"""
QUESTION:
Create a function `count_pairs_divisible_by_3` that takes a list of integers as input and returns the count of pairs whose sum is divisible by 3. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list. The input list will contain at least two integers and may include duplicate and negative integers.
"""

def count_pairs_divisible_by_3(lst):
    counts = [0] * 3
    for num in lst:
        counts[num % 3] += 1

    count_pairs = 0
    count_pairs += counts[0] * (counts[0] - 1) // 2
    count_pairs += counts[1] * (counts[1] - 1) // 2
    count_pairs += counts[2] * (counts[2] - 1) // 2
    count_pairs += counts[0] * counts[1]
    count_pairs += counts[0] * counts[2]
    count_pairs += counts[1] * counts[2]
    return count_pairs