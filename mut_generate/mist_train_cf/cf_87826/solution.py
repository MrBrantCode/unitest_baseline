"""
QUESTION:
Create a function called `bubble_sort` that takes a list of numbers as input, sorts the list in ascending order, and groups duplicates together based on their values. Additionally, the function should sort the duplicates in ascending order based on the sum of their digits. The function should return the sorted list.
"""

def get_digit_sum(num):
    return sum(int(digit) for digit in str(num))

def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    sorted_nums = []
    start_index = 0
    while start_index < len(nums):
        end_index = start_index + 1
        while end_index < len(nums) and nums[start_index] == nums[end_index]:
            end_index += 1
        sublist = nums[start_index:end_index]
        sublist.sort(key=get_digit_sum)
        sorted_nums.extend(sublist)
        start_index = end_index
    
    return sorted_nums