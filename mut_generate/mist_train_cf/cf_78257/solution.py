"""
QUESTION:
Write a function named `convert_to_number` that takes a list of strings representing numbers, including potentially erroneous formats, and returns the maximum, minimum, and average of the valid numbers in the list. The function should handle potential errors by ignoring non-numeric strings and avoiding division by zero when calculating the average.
"""

def convert_to_number(nums):
    def convert_to_num(s):
        try:
            return float(s)
        except ValueError:
            return None
        
    nums = [convert_to_num(i) for i in nums]
    nums = [i for i in nums if i is not None]

    if len(nums) > 0:
        return max(nums), min(nums), sum(nums)/len(nums)
    else:
        return "No numbers found in the list."