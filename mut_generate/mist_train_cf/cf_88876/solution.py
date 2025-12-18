"""
QUESTION:
Write a function `delete_5th_prime(lst)` to delete the 5th prime number from a list of up to 10,000,000 elements. The function should not use any built-in functions or methods that directly delete elements from a list, handle duplicate elements, and optimize for time complexity. If the list has less than 5 prime numbers, the function should print a corresponding message. It should also handle cases where the list is empty or has less than 5 elements.
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
                lst = lst[:index] + lst[index + 1:]
                break
        index += 1
    
    if count < 5:
        print("List has less than 5 prime numbers.")
    elif len(lst) < 5:
        print("List has less than 5 elements.")
    elif len(lst) == 0:
        print("List is empty.")
    return lst