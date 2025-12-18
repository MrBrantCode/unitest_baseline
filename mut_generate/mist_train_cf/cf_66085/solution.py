"""
QUESTION:
Create a function `identify_primes` that takes two lists, `nums` and `bools`, as input. `nums` contains integers and `bools` contains boolean values with the same length as `nums`. Return a list of tuples, where each tuple contains the index and value of a prime number in `nums` for which the corresponding boolean entry in `bools` is True. Note that the output should include non-prime numbers if their corresponding boolean values are True, contradicting the function's name.
"""

def identify_primes(nums, bools):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = [(i, num) for i, (num, bool_val) in enumerate(zip(nums, bools)) if bool_val and is_prime(num)]

    return result