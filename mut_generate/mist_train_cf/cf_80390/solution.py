"""
QUESTION:
Write a function `find_trailing_zeros(n: int) -> int` that calculates the quantity of trailing zeros in the output of the factorial of a given number `n`. The function should be optimized for large calculations (up to 10^8) and should not directly calculate the factorial. Implement the function to minimize the number of iterations necessary.
"""

def find_trailing_zeros(n: int) -> int:
    count = 0 
      
    # Keep dividing n by powers of  
    # 5 and update count 
    while n >= 5: 
        n //= 5 # floor division
        count += n 
  
    return count