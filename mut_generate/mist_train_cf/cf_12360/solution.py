"""
QUESTION:
Write a function called `reverse_odd` that takes an array of positive integers as input, reverses the order of only the odd integers, keeps even integers in their original positions, and returns the resulting array in descending order.
"""

def reverse_odd(arr):
    odd_arr = [num for num in arr if num % 2 == 1][::-1]
    result = []
    odd_index = 0
    
    for num in sorted(arr, reverse=True):
        if num % 2 == 1:
            result.append(odd_arr[odd_index])
            odd_index += 1
        else:
            result.append(num)
    
    return result