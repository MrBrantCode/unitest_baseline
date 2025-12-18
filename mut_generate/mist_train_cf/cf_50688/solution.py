"""
QUESTION:
Create a function named `generate_array` that generates a two-dimensional array of integers containing all the prime numbers and their multiples (up to that prime number) between 1 and 250. The result should be such that the prime number is the first element of each sub-array and the subsequent elements are its multiples.
"""

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_array():
    array = []
    for num in range(1, 251):
        if is_prime(num):
            sub_array = [num*i for i in range(1, num+1) if num*i <= 250]
            array.append(sub_array)
    return array