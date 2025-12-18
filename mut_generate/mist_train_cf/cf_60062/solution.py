"""
QUESTION:
Write a function `find_primes` that takes a string of semicolon-separated integers as input and returns a string of the prime numbers from the input, also separated by semicolons. The input string may contain leading or trailing spaces around the semicolons. Assume that the input string is well-formed and contains only integers separated by semicolons.
"""

def find_primes(input_string):
    def is_prime(num):
        if num < 2:  
            return False
        for i in range(2,int(num**0.5) + 1):  
            if num % i == 0:  
                return False
        return True  

    numbers = input_string.split(';')
    numbers = [int(num.strip()) for num in numbers]  
    primes = [num for num in numbers if is_prime(num)]  
    primes_string = '; '.join(map(str,primes))  
    return primes_string