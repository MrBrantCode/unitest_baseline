"""
QUESTION:
Implement a function `merge_sort` that takes a list of numbers as input and returns the sorted list using the merge sort algorithm. The function should recursively divide the input list into two halves until each sublist contains one element, then merge the sublists back together in sorted order.
"""

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_list = nums[:mid]
    right_list = nums[mid:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge(left_list, right_list)


def merge(left_list, right_list):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            sorted_list.append(left_list[left_index])
            left_index += 1
        else:
            sorted_list.append(right_list[right_index])
            right_index += 1

    sorted_list += left_list[left_index:]
    sorted_list += right_list[right_index:]

    return sorted_list