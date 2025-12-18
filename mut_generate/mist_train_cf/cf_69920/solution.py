"""
QUESTION:
Develop a function named lcm_three_numbers that calculates the least common multiple (LCM) of three numbers. The function should handle negative integers and return -1 for any invalid input (zero or non-integer values). The function should be able to handle large integers up to the range of 10^18.
"""

def lcm_three_numbers(a, b, c):
    
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int) and a != 0 and b != 0 and c != 0:  
        def gcd(x, y):
            while(y):
                x, y = y, x % y
            return x

        def lcm(x, y):
            lcm = (x*y)//gcd(x,y)
            return lcm

        return lcm(lcm(a, b), c)
    else:
        return -1