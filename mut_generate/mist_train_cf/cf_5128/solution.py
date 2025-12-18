"""
QUESTION:
Create a function `copy_smaller_primes` that takes an array and returns a new array containing prime numbers from the input array that are smaller than 5, with a maximum length of 5. If no such prime numbers exist, return an empty array. Implement the solution using recursion.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def copy_smaller_primes(input_array):
    def helper(input_array, new_array, index):
        if index == len(input_array) or len(new_array) == 5:
            return new_array
        if input_array[index] < 5 and is_prime(input_array[index]):
            new_array.append(input_array[index])
        return helper(input_array, new_array, index + 1)
    
    return helper(input_array, [], 0)