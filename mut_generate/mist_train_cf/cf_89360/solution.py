"""
QUESTION:
Write a function named `delete_largest_prime` that takes a list of positive integers as input, finds the largest prime number in the list, deletes all occurrences of it, and returns the modified list. The function should not take any other parameters besides the input list.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def delete_largest_prime(my_list):
    largest_prime = 0
    for num in my_list:
        if is_prime(num) and num > largest_prime:
            largest_prime = num
    
    modified_list = [num for num in my_list if num != largest_prime]
    return modified_list