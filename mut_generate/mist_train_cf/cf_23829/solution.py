"""
QUESTION:
Write a function `prime_factors(n)` that finds all the prime factors of a given integer `n`. The function should return a list of prime factors. The input `n` is a positive integer, and the output list should contain the prime factors in any order.
"""

def prime_factors(n):
    # Empty list to store prime factors 
    lst = [] 
    
    # Divide by 2 while the number is 
    # divisible by 2  
    while n % 2 == 0: 
        lst.append(2)
        n = n / 2
          
    # n must be odd, now 
    # check all the numbers from 3 to 
    # the square root of n  
    for i in range(3, int(n**0.5)+1): 
        # check for divisibility of i by n  
        while n % i== 0: 
            lst.append(i) 
            n = n / i 
          
    # If n is a prime number then it 
    # will only be divisible by itself  
    if n > 2:
        lst.append(n)
      
    return lst