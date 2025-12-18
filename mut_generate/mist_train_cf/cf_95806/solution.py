"""
QUESTION:
Write a function `reverse_odd_sort(arr)` that takes an array of positive integers and returns a new array. In the new array, the odd integers from the original array should be reversed and sorted in descending order, while the even integers should remain in their original positions. The function should have a time complexity of O(n) and should not use any built-in sorting functions or libraries.
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