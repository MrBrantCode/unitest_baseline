"""
QUESTION:
Write a function `print_list_info(nums)` that takes a list of integers `nums` as input. The function should print the maximum and minimum values from the list. If the list is empty, it should print an error message and stop execution. It should also remove any duplicate values from the list, print the resulting list, and then print the frequency of each remaining value in the original list.
"""

def print_list_info(nums):
    if len(nums) == 0:
        print("Error: List is empty.")
        return
    
    max_value = max(nums)
    min_value = min(nums)
    print("Max value:", max_value)
    print("Min value:", min_value)
    
    unique_nums = list(set(nums))
    print("Duplicate-free list:", unique_nums)
    
    print("Duplicate values and their frequencies:")
    for num in unique_nums:
        frequency = nums.count(num)
        print("-", num, "(", frequency, "times)")