"""
QUESTION:
Write a function `swap_even_odd(arr)` that takes an array of integers as input. The function should swap the even and odd elements in the array while maintaining their original order and calculate the sum of the even elements. The input array must have a length of at least 10 and only contain positive integers. If the input array does not meet these requirements, the function should return an error message.
"""

def swap_even_odd(arr):
    if len(arr) < 10:
        return "Error: Input array length should be at least 10."
    
    for i in range(len(arr)):
        if arr[i] <= 0:
            return "Error: Input array should only contain positive integers."
    
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            for j in range(i+1, len(arr)):
                if arr[j] % 2 != 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    break

    sum_even = sum([x for x in arr if x % 2 == 0])
    return arr, sum_even