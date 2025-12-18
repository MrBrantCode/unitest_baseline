"""
QUESTION:
Write a function `special_concat` that takes an array of integers as input. The function should iterate over the array in steps of 2, exponentiate the elements in each pair (first element to the power of the second element), sum the results, convert the sum to a string, concatenate it with the string '1111111', and return the result as an integer. If the array is empty, the function should return 1111111. The function should handle arrays with both even and odd numbers of elements efficiently, with a time complexity of O(n), where n is the length of the array.
"""

def special_concat(arr):
    total = 0
    for i in range(0, len(arr) - len(arr) % 2, 2): 
        total += arr[i] ** arr[i + 1]       
    if len(arr) % 2:                        
        total += arr[-1]       
    return int(str(total) + '1111111')      