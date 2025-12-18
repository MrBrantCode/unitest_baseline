"""
QUESTION:
Implement a function named `bubble_sort` that takes an array of integers as input, sorts it in ascending order using the bubble sort algorithm, and returns the sorted array. The function should optimize the process by stopping the algorithm if no swaps are made in a pass, indicating that the array is already sorted.
"""

def bubble_sort(nums):
    # Get the length of the list
    length = len(nums)
    
    # Start a loop
    for i in range(length):
        # Set a flag to false
        flag = False
        # Start another loop from the start to the length minus i minus 1
        for j in range(0, length - i - 1):
            # If the current number is greater than the next one
            if nums[j] > nums[j + 1]:
                # Swap them
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                # Set the flag to true
                flag = True
        # If the flag is still false after the inner loop
        if not flag:
            # Break the loop because the list is already sorted
            break
    return nums