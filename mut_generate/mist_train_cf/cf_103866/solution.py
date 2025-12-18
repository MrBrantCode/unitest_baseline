"""
QUESTION:
Create a function `swap_prime_elements(lst, index_1, index_2)` that takes in a list of integers `lst` and two indices `index_1` and `index_2`. The function should swap the elements at `index_1` and `index_2` in the list if both elements are prime numbers. If either of the elements is not prime or if the indices are out of range, return the original list unchanged.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def swap_prime_elements(lst, index_1, index_2):
    if index_1 < 0 or index_1 >= len(lst) or index_2 < 0 or index_2 >= len(lst):
        return lst
    
    if is_prime(lst[index_1]) and is_prime(lst[index_2]):
        lst[index_1], lst[index_2] = lst[index_2], lst[index_1]
    
    return lst