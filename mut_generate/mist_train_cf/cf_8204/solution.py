"""
QUESTION:
Write a function `modify_array` that takes an array of at least 6 integers and an index as input. If the index is 4, check if the number at that index is prime using the recursive function `is_prime`. If it is prime, multiply it by 2; otherwise, add 1 to it. The function should recursively call itself to check the next index until it has checked all indices in the array.
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