"""
QUESTION:
Write a function named `sum_odd_digits` that takes a 3-digit number `num` as input, where `10^2 <= num <= 10^9`. The function should calculate the sum of the products of each odd digit in `num` with the corresponding digit from the reverse of `num`, excluding any odd digits that are prime numbers. If there are no odd digits in `num` or if all the odd digits are prime numbers, the function should return -1.
"""

def sum_odd_digits(num):
    def is_prime(digit):
        if digit < 2:
            return False
        for i in range(2, int(digit ** 0.5) + 1):
            if digit % i == 0:
                return False
        return True

    result = 0
    str_num = str(num)
    rev_num = int(str_num[::-1])
    
    for i, digit in enumerate(str_num):
        digit = int(digit)
        if digit % 2 != 0 and not is_prime(digit):
            result += digit * int(str(rev_num)[i])
    
    return -1 if result == 0 else result