"""
QUESTION:
Create a function called `create_array` that takes two parameters, `rows` and `cols`, representing the dimensions of a 2D array. The function should return a 2D array of size `rows` x `cols`, where all elements are unique, in ascending order, and are prime numbers. The function should not use any built-in libraries or functions to check for prime numbers and should have a time complexity of O(n), where n is the total number of elements in the array.
"""

def create_array(rows, cols):
    prime_array = []
    num = 2
    while len(prime_array) < rows * cols:
        if num > 1 and all(num % i for i in range(2, int(num**0.5) + 1)):
            prime_array.append(num)
        num += 1
    return [prime_array[i*cols : (i+1)*cols] for i in range(rows)]