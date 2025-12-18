"""
QUESTION:
Write a function `delete_fifth_prime` that takes a list of integers as input and returns the list after deleting the 5th prime number. If the list has less than 5 prime numbers, return the original list. The function should modify the input list in-place and optimize for time complexity. The function should not use any built-in functions or methods that directly delete elements from a list.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def delete_fifth_prime(numbers):
    count = 0
    for i, num in enumerate(numbers):
        if is_prime(num):
            count += 1
        if count >= 5:
            break
    if count < 5:
        return numbers

    delete_index = None
    count = 0
    for i, num in enumerate(numbers):
        if is_prime(num):
            count += 1
        if count == 5:
            delete_index = i
            break
    if delete_index is None:
        return numbers

    shift = 1
    for i in range(delete_index + 1, len(numbers)):
        numbers[i - shift] = numbers[i]
    del numbers[-shift:]
    return numbers