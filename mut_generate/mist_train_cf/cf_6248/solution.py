"""
QUESTION:
Write a function called `get_random_divisible_by_2_and_greater_than_10` that takes a list of unique integers as input and returns a random value from the list that is greater than 10 and divisible by 2. The function should also remove the selected value from the input list. The list will contain between 10 and 100 integers. Do not use any built-in random number generation functions or libraries. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def get_random_divisible_by_2_and_greater_than_10(nums):
    valid_nums = [num for num in nums if num > 10 and num % 2 == 0]
    seed = sum(valid_nums)  # Using a simple seed for demonstration purposes
    index = (seed % len(valid_nums))  # Simple modulo operation to ensure index is within range
    selected_num = valid_nums[index]
    nums.remove(selected_num)
    return selected_num