"""
QUESTION:
Write a function named `check_even_prime` that takes a non-negative integer `n` as input. The function should print out whether the number is even or not. If the number is even, it should also determine and print whether it's prime or not. Additionally, it should return a boolean flag indicating the prime status of the even number. The function should be able to handle large input numbers, such as 10^6.
"""

def check_even_prime(n):
    def is_prime(num):
        if num < 2: 
            return False
        if num == 2: 
            return True    
        if num % 2 == 0: 
            return False    
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    if n % 2 == 0:
        print("Yes, it's even")
        prime_status = is_prime(n)
        if prime_status:
            print("Yes, it's prime")
        else:
            print("No, it's not prime")
    else:
        print("No, it's not even")
        prime_status = None

    return prime_status