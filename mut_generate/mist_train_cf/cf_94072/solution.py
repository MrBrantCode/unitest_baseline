"""
QUESTION:
Write a function called `print_list_info` that takes a list of integers as input. The function should first check if the list is empty. If the list is empty, it should print "Error: List is empty." and stop execution. If the list is not empty, it should find the maximum and minimum values in the list and print them. Then, it should remove duplicate values from the list and print the resulting list. Finally, it should print the frequency of each value in the original list.
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