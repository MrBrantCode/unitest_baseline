"""
QUESTION:
Combine two lists of positive integers, remove duplicates, sort the resulting list in descending order, and filter it to include only prime numbers with non-repeating digits. 

The function should take two lists of integers as input and return a list of integers. The prime numbers should be checked using a helper function, and the non-repeating digits condition should also be checked using a helper function.
"""

def combine_and_filter(list1, list2):
    def check_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def check_digits(n):
        digits = list(str(n))
        return len(digits) == len(set(digits))

    combined = list(set(list1 + list2))
    combined.sort(reverse=True)
    return [i for i in combined if check_prime(i) and check_digits(i)]