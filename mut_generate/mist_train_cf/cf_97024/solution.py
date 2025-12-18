"""
QUESTION:
Create a function `check_conditions` that takes an integer `num` as input and returns `True` if the number is a multiple of both 5 and 7, greater than 100, and has exactly three distinct prime factors. Otherwise, it should return `False`.
"""

def check_conditions(num):
    count = 0
    prime_factors = set()
    
    if num % 5 == 0 and num % 7 == 0 and num > 100:
        for i in range(2, num+1):
            if num % i == 0:
                count += 1
                prime_factors.add(i)
            if count > 3:
                return False
                
        if len(prime_factors) == 3:
            return True
        else:
            return False
    else:
        return False