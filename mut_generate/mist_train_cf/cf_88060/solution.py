"""
QUESTION:
Write a function called `find_median` that calculates the median of a list of integers, where the list may contain duplicates. The function must have a time complexity of O(n) and must not use any built-in sorting functions or data structures.
"""

def find_median(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    sorted_count = sorted(count.items(), key=lambda x: x[1])
    max_count = max(count.values())
    max_count_nums = [num for num, cnt in sorted_count if cnt == max_count]

    if len(max_count_nums) % 2 == 1:
        median = max_count_nums[len(max_count_nums) // 2]
    else:
        median = (max_count_nums[len(max_count_nums) // 2 - 1] + max_count_nums[len(max_count_nums) // 2]) / 2

    return median