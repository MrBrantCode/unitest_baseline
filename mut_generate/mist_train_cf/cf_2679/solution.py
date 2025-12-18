"""
QUESTION:
Write a function `remove_duplicates_sort_descending` that takes a list of integers as input, removes duplicates, and returns the remaining elements in descending order. The function should have a time complexity of O(nlogn) or better and should not use the built-in `set` function or the `sort` method. The function should also preserve the original order of elements when removing duplicates, and the sorting should be based on the values of the elements, not their frequencies.
"""

def remove_duplicates_sort_descending(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    sorted_list = []
    for key, value in frequency.items():
        sorted_list.append((key, value))

    sorted_list.sort(reverse=True, key=lambda x: x[0])

    result = []
    for item in sorted_list:
        result.extend([item[0]] * item[1])

    return result