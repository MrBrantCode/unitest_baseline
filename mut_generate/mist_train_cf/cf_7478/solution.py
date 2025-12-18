"""
QUESTION:
Create a function called `generate_array` that takes a string of integers as input and returns an array of integers. The function should calculate the sum of each integer and its neighbors that are divisible by 2, treating consecutive even numbers as a single number. The resulting array should be sorted in descending order, contain no duplicates, and include only sums that are divisible by 2. If the input string is empty, return an empty array. If the input string contains non-numeric characters, return an error message indicating the invalid characters found.
"""

def generate_array(s):
    if len(s) == 0:
        return []

    for char in s:
        if not char.isdigit():
            return "Invalid characters found: {}".format(char)

    nums = [int(char) for char in s]

    i = 0
    while i < len(nums) - 1:
        if nums[i] % 2 == 0 and nums[i] == nums[i + 1]:
            nums.pop(i)
        else:
            i += 1

    result = []

    for i in range(len(nums)):
        left = nums[i-1] if i > 0 and nums[i-1] % 2 == 0 else 0
        right = nums[i+1] if i < len(nums)-1 and nums[i+1] % 2 == 0 else 0
        sum_neighbors = left + right + nums[i]
        if sum_neighbors % 2 == 0:
            result.append(sum_neighbors)

    result = list(set(result))
    result.sort(reverse=True)

    return result