"""
QUESTION:
Write a function `find_last_prime_not_multiple_of_five(lst)` that takes a list of integers `lst` as input and returns the last prime number in the list that is not a multiple of 5. The input list will have at least one non-multiple of 5 prime number. The function should be able to handle extremely large numbers without overflowing.
"""

def find_last_prime_not_multiple_of_five(lst):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    result = [x for x in lst if is_prime(x) and x % 5 != 0]
    return result[-1] if result else None