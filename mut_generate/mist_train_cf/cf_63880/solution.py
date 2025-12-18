"""
QUESTION:
Create a function `find_sums(nums)` that takes a list of integers as input, calculates the cumulative sum of individual digits for each integer (preserving the negative sign), and returns a dictionary mapping each integer to its sum, as well as lists of integers with the maximum and minimum sums.
"""

def find_sums(nums):
    # Calculate the sum of individual digits for each integer
    sums = [sum(map(int, str(num))) if num >= 0 else -sum(map(int, str(abs(num)))) for num in nums]

    # Create a dictionary where the keys are integers and the values are their sums
    sums_dict = dict(zip(nums, sums))

    # Find the maximum and minimum sums
    max_sum = max(sums_dict.values())
    min_sum = min(sums_dict.values())

    # Find the integers with maximum and minimum sums
    max_nums = [num for num, s in sums_dict.items() if s == max_sum]
    min_nums = [num for num, s in sums_dict.items() if s == min_sum]

    return sums_dict, max_nums, min_nums