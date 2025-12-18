"""
QUESTION:
Write a function called `bubble_sort` that sorts a list of numbers in ascending order. If there are duplicates in the list, ensure they are grouped together and sorted in ascending order based on the sum of their digits. The `bubble_sort` function should take a list of numbers as input and return the sorted list. The function should use bubble sort as its sorting algorithm and handle duplicates as described above.
"""

def bubble_sort(nums):
    def get_digit_sum(num):
        return sum(int(digit) for digit in str(num))

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