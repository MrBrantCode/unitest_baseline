"""
QUESTION:
Write a function `removeDuplicates` that takes an array of integers as input and returns a new array containing the unique integers from the input array. The function should have a time complexity of O(n) and use only constant space. The input array can contain integers ranging from -10^5 to 10^5 and can have a maximum length of 10^4.
"""

def removeDuplicates(nums):
    unique_set = set()
    result = []

    for num in nums:
        if num not in unique_set:
            unique_set.add(num)
            result.append(num)

    return result