"""
QUESTION:
Write a function `delete_5th_prime` that takes a list of integers as input and deletes the 5th prime number from the list in-place. The function should not use any built-in functions or methods that directly delete elements from a list. It should handle cases where the list is empty, has less than 5 elements, or has less than 5 prime numbers. The function should also be optimized for time complexity and be able to handle lists with up to 10,000,000 elements.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def delete_5th_prime(lst):
    count = 0
    index = 0
    for i in range(len(lst)):
        if is_prime(lst[i]):
            count += 1
            if count == 5:
                lst[index:index+1] = []
                break
        index += 1
    return lst