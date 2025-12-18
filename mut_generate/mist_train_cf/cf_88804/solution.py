"""
QUESTION:
Create a function `copy_smaller_primes(input_array, new_array, index)` that creates a new array consisting of prime numbers from the input array, where the numbers are smaller than 5 and the length of the new array does not exceed 5. Implement this function using recursion.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def copy_smaller_primes(input_array, new_array, index):
    # Base cases
    if index == len(input_array) or len(new_array) == 5:
        return new_array
    
    # Recursive case
    if input_array[index] < 5 and is_prime(input_array[index]):
        new_array.append(input_array[index])
    
    return copy_smaller_primes(input_array, new_array, index + 1)