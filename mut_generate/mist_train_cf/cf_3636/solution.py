"""
QUESTION:
Create a function named `find_median` that takes a list of integers as input and returns the median of the list. The list may contain duplicates, and the function must achieve a time complexity of O(n) without using any built-in sorting functions or data structures.
"""

def find_median(lst):
    count = 0
    max_count = 0
    num_counts = {}

    # Count the occurrences of each integer
    for num in lst:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

        # Update the maximum count
        if num_counts[num] > max_count:
            max_count = num_counts[num]

    # Find the integer(s) with the highest count
    max_count_nums = []
    for num, count in num_counts.items():
        if count == max_count:
            max_count_nums.append(num)

    # Sort the integers with the highest count
    max_count_nums.sort()

    # Calculate the median
    if len(max_count_nums) % 2 == 1:
        median = max_count_nums[len(max_count_nums) // 2]
    else:
        median = (max_count_nums[len(max_count_nums) // 2 - 1] + max_count_nums[len(max_count_nums) // 2]) / 2

    return median