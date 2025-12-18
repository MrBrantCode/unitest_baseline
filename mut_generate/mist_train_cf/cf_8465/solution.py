"""
QUESTION:
Write a function `add_prime_to_array(arr, prime)` that takes an array of integers and a prime number greater than 100 as input parameters. The function should add the prime number to every element in the array and return the product of all the elements in the resulting array.
"""

def add_prime_to_array(arr, prime):
    result = [num + prime for num in arr]
    product = 1
    for num in result:
        product *= num
    return product