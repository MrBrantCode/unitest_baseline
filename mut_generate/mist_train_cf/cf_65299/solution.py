"""
QUESTION:
Implement a function named `find_emirps` that takes one parameter `n` and returns a list of the first `n` emirps, where an emirp is a non-palindromic prime number that becomes a different prime number when its digits are reversed. The function should check for the correctness of the given number `n` before starting the calculation and should be efficient with respect to time and space complexity. The input `n` should be a positive integer, and the function should return `None` if `n` is not greater than 0.
"""

def find_emirps(n):
    if n < 1:
        return None
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    emirps = []
    num = 13
    while len(emirps) < n:
        if (str(num) != str(num)[::-1]) and is_prime(num) and is_prime(int(str(num)[::-1])):
            emirps.append(num)
        num += 1
    return emirps