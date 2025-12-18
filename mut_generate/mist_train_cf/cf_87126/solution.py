"""
QUESTION:
Write a function `sum_of_elements(arr)` that calculates the sum of the elements in the given array `arr` that meet the following conditions:
- The element is divisible by both 2 and 3.
- The element is a prime number.
- The sum of the digits of the element is a prime number.
The function should return the calculated sum.
"""

def sum_of_elements(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = 0
    for num in arr:
        if num % 2 == 0 and num % 3 == 0 and is_prime(num) and is_prime(sum(int(digit) for digit in str(num))):
            result += num
    return result