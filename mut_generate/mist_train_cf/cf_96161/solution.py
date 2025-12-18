"""
QUESTION:
Write a function `find_kth_largest(nums, k)` that takes an unsorted array of unique positive integers `nums` and an integer `k` as input, and returns the kth largest element in the array. The array will contain at most 10^5 elements, and all elements will be unique positive integers ranging from 1 to 10^9. Implement a more efficient algorithm that does not require sorting the entire array.
"""

def find_kth_largest(nums, k):
    # Helper function to partition the array
    def partition(nums, low, high):
        pivot = nums[high]  # Select the last element as the pivot
        i = low - 1  # Index of the smaller element

        for j in range(low, high):
            if nums[j] >= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quickselect(nums, low, high, k):
        if low == high:  # Base case: only one element
            return nums[low]

        pivot_index = partition(nums, low, high)

        if pivot_index == k - 1:  # Found the kth largest element
            return nums[pivot_index]
        elif pivot_index < k - 1:  # Recurse on the right half
            return quickselect(nums, pivot_index + 1, high, k)
        else:  # Recurse on the left half
            return quickselect(nums, low, pivot_index - 1, k)

    # Call the quickselect function with the initial bounds
    return quickselect(nums, 0, len(nums) - 1, k)