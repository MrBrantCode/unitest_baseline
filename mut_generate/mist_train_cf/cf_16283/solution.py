"""
QUESTION:
Create a function `get_sorted_odd_numbers` that takes a list of integers as input, extracts the odd numbers, removes duplicates, and returns the resulting list in descending order without using built-in sorting or duplicate removal functions. The function should only return a list of unique odd numbers in descending order.
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