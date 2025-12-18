"""
QUESTION:
Implement a function `quick_sort(nums, low, high)` that sorts an array of integers using the quick sort algorithm. The function should take as input an array `nums` and two indices `low` and `high` representing the range of the array to be sorted. The function should sort the array in-place, i.e., it should not create a new array, but rather modify the original array.
"""

def quick_sort(nums, low, high):
    def partition(nums, low, high):
        i = low - 1
        pivot = nums[high]

        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    if low < high:
        part_idx = partition(nums, low, high)
        quick_sort(nums, low, part_idx - 1)
        quick_sort(nums, part_idx + 1, high)