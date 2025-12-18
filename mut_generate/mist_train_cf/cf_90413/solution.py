"""
QUESTION:
Write a function named `add_prime_to_array` that takes an array of integers and a prime number greater than 100 as input, adds the prime number to every element in the array, and returns the product of all the elements in the resulting array. The function must handle the calculation of the product internally and not rely on any external libraries or built-in functions for this purpose.
"""

def add_prime_to_array(arr, prime):
    result = []
    for num in arr:
        result.append(num + prime)
    product = 1
    for num in result:
        product *= num
    return product