"""
QUESTION:
Create a function named `even_prime_nums` that takes two parameters, `min_num` and `max_num`, representing the range of numbers to check. The function should return a dictionary where each key is an even number between `min_num` and `max_num` (inclusive) and the corresponding value is a boolean indicating whether the even number is prime or not. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
"""

def even_prime_nums(min_num, max_num):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    even_prime_dict = {}
    for num in range(min_num, max_num + 1):
        if num % 2 == 0:
            even_prime_dict[num] = is_prime(num)
    return even_prime_dict