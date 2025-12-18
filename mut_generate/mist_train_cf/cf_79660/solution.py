"""
QUESTION:
Write a function `first_prime(lst)` that takes a list of numerical values as input, identifies the first prime number within the list, and returns it. If the list is empty or does not contain any prime numbers, return the message "There is no prime number in the list." The function should only consider integers in the list and ignore non-integer values.
"""

def first_prime(lst):
    def check_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n%2 == 0 or n%3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n%i == 0 or n%(i + 2) == 0:
                return False
            i += 6
        return True

    for i in lst:
        if isinstance(i, int): 
            if check_prime(i): 
                return i
    return "There is no prime number in the list."