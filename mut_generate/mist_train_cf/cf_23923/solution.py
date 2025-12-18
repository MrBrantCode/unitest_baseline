"""
QUESTION:
Write a function named 'calculate_mode_and_median' that takes a list of integers as input and returns both the mode (the number that appears most frequently) and the median (the middle value in the sorted list). The mode will be the smallest number in case of a tie.
"""

def calculate_mode_and_median(nums):
    nums.sort()
    n = len(nums)
    
    # calculate median
    median = nums[n // 2] if n % 2 else (nums[n // 2 - 1] + nums[n // 2]) / 2
    
    # calculate mode
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    max_count = max(count.values())
    mode = min([num for num, freq in count.items() if freq == max_count])
    
    return mode, median