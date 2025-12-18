"""
QUESTION:
Create a function `modify_array(arr, index)` that takes an array of at least 6 elements and an index as parameters. The function should check if the item at index 4 is a prime number using a recursive function `is_prime(n)`. If the item is a prime number, multiply it by 2; otherwise, add 1 to it. The `modify_array` function should also be recursive, modifying the array in-place and returning the modified array.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def modify_array(arr, index):
    if index >= len(arr):
        return arr
    if index == 4:
        if is_prime(arr[index]):
            arr[index] *= 2
        else:
            arr[index] += 1
    return modify_array(arr, index + 1)