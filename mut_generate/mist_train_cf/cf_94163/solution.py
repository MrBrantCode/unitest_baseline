"""
QUESTION:
Create a function `get_sorted_odd_numbers` that takes a list of integers as input. The function should return a list containing only the unique odd numbers from the input list, sorted in descending order, without using built-in functions or methods for sorting or removing duplicates.
"""

def get_sorted_odd_numbers(nums):
    # Create a set to store unique odd numbers
    odd_nums = set()

    # Iterate through the input list and add odd numbers to the set
    for num in nums:
        if num % 2 != 0:
            odd_nums.add(num)

    # Convert the set back to a list
    odd_nums = list(odd_nums)

    # Sort the list in descending order using bubble sort algorithm
    n = len(odd_nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if odd_nums[j] < odd_nums[j+1]:
                odd_nums[j], odd_nums[j+1] = odd_nums[j+1], odd_nums[j]

    return odd_nums