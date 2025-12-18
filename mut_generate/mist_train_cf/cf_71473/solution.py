"""
QUESTION:
Write a function `starts_one_ends(n, x, y)` that calculates the quantity of n-length positive integers that begin and conclude with 1, are inherently divisible by both 3 and 5, and exclude both x and y at any position in their sequence. The function should take three parameters: a positive integer `n`, and two non-negative integers `x` and `y`. The function should return the count of integers that meet the specified conditions.
"""

def starts_one_ends(n, x, y) :
    count = 0
    start = 10**(n-1)
    end = 10**n
    x = str(x)
    y = str(y)
    
    for i in range(start, end) :
        if i%5 == 0 and i%3 == 0 :
            s = str(i)
            if s[0] == '1' and s[-1] == '1' :
                if x not in s and y not in s :
                    count += 1
    return count