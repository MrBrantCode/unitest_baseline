"""
QUESTION:
Write a function called `reverse_odd_sort` that takes in an array of positive integers and returns a new array where the elements are reversed if they are odd integers. The odd integers should be sorted in descending order, while even integers should remain in their original position. The function must have a time complexity of O(n), where n is the length of the input array, and cannot use any built-in sorting functions or libraries.
"""

def reverse_odd_sort(arr):
    odd_nums = []
    for num in arr:
        if num % 2 == 1:
            odd_nums.append(num)
    odd_nums.sort(reverse=True)

    result = []
    i = 0
    for num in arr:
        if num % 2 == 1:
            result.append(odd_nums[i])
            i += 1
        else:
            result.append(num)
    
    return result