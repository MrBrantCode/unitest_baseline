"""
QUESTION:
Write a function named `print_primes(n)` that prints all prime numbers between 1 and `n` using recursion, with a time complexity of O(log n) and a space complexity of O(1).
"""

def print_primes(n):
    def is_prime(num):
        if num < 2:  
            return False
        if num == 2:  
            return True
        if num % 2 == 0:  
            return False

        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2  

        return True

    def helper(k):
        if k < 2:  
            return
        else:
            helper(k - 1)  

        if is_prime(k):
            print(k)  

    helper(n)