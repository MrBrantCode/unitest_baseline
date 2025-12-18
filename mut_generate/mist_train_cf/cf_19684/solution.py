"""
QUESTION:
Write a function `find_most_frequent(nums, m)` that finds the most frequently occurring item in a list of integers `nums`, where the length of `nums` is n and each integer is in the range of 1 to m. The function should have a time complexity of O(n) and a space complexity of O(m), and should not use any additional data structures or built-in functions, such as dictionaries or collections.
"""

def find_most_frequent(nums, m):
    counts = [0] * (m + 1)
    max_count = 0
    max_item = 0

    for num in nums:
        counts[num] += 1
        if counts[num] > max_count:
            max_count = counts[num]
            max_item = num

    return max_item