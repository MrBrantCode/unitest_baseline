"""
QUESTION:
Create a function `create_array(rows, cols)` that generates a 2D array of dimensions `rows` x `cols` where all elements are unique prime numbers in ascending order. The function should not use any built-in libraries or functions to check for prime numbers and must have a time complexity of O(n) or better, where n is the total number of elements in the array.
"""

def create_array(rows, cols):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_array = []
    num = 2
    while len(prime_array) < rows * cols:
        if is_prime(num):
            prime_array.append(num)
        num += 1
    array = []
    for i in range(rows):
        row = prime_array[i*cols : (i+1)*cols]
        array.append(row)
    return array