"""
QUESTION:
Create a function called `count_primes` that takes two parameters, `start_num` and `end_num`, and returns the number of prime numbers between `start_num` and `end_num` (inclusive), where prime numbers are greater than 1 and less than or equal to 100. If `start_num` is greater than `end_num`, the function should return an error message.
"""

def count_primes(start_num, end_num):
    if start_num > end_num:
        return "Error: start_num is greater than end_num"
    
    start_num = max(start_num, 2)
    end_num = min(end_num, 100)
    
    count = 0
    for num in range(start_num, end_num+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    
    return count