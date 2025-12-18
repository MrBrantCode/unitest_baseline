"""
QUESTION:
Create a function called `find_median` that takes a list of numbers as input and returns the median of the list. The function must first manually sort the list in descending order without using any built-in sorting functions. After sorting, the function should calculate and return the median, which is the middle number if the list has an odd number of elements, or the average of the two middle numbers if the list has an even number of elements.
"""

def find_median(nums):
    # First we need to sort the list in descending order
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Swap if the element found is greater than the next element
            if nums[i] < nums[j] :
                nums[i], nums[j] = nums[j], nums[i]

    # After sorting check if the length of list is odd or even
    n = len(nums)
    middle = n // 2
    # If length is odd, return middle element
    if n % 2:
        return nums[middle]
    # If length is even, return average of middle elements
    return (nums[middle - 1] + nums[middle]) / 2