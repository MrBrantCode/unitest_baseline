"""
QUESTION:
Write a function `switch` that takes two lists of integers, `lst1` and `lst2`, as input. The function should determine if it's possible to perform a one-to-one interchange of elements between the lists such that `lst1` exclusively comprises prime numbers without affecting the total sum of both lists. Return "YES" if this is achievable, or "NO" if it isn't. Assume that the input lists are non-empty and the interchange is limited to a 1-to-1 swap, where one element from `lst1` can only be swapped with one element from `lst2`.
"""

def switch(lst1, lst2):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if sum(lst1) != sum(lst2):
        return "NO"

    not_prime_lst1 = [num for num in lst1 if not is_prime(num)]
    lst1 = [num for num in lst1 if is_prime(num)]
    lst2.extend(not_prime_lst1)

    for num in lst2:
        if sum(lst1) + num != sum(lst2):
            return "NO"
    return "YES"