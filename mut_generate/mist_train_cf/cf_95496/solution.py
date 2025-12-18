"""
QUESTION:
Create a function `create_dict` that takes two lists `list1` and `list2` as input. `list1` contains only strings with lowercase alphabetic characters and `list2` contains only positive integers not exceeding 100. The function should return a dictionary created by pairing corresponding elements from `list1` and `list2` using the zip() function, but only if the sum of all integers in `list2` is a prime number. If the sum is not prime, the function should print an error message and return `None`. The function should not take any other input and should not modify the input lists.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def create_dict(list1, list2):
    if not is_prime(sum(list2)):
        print("Error: The sum of all integers in list2 is not a prime number.")
        return None
    return dict(zip(list1, list2))