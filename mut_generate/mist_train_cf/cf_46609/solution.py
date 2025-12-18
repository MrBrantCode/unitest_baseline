"""
QUESTION:
Implement a function `Karatsuba(x, y)` that multiplies two large numbers `x` and `y` represented as integers, without using built-in multiplication or big integer library functions. The function should be able to handle inputs with a length of 1 ≤ n ≤ 10^6.
"""

def multiplyKaratsuba(x, y):
    
    # size of the numbers
    if x<10 and y<10:
        return x*y

    # finds the size of the numbers
    m = max(len(str(x)), len(str(y)))
    m2 = m // 2

    # divide the numbers in half
    high1, low1 = divmod(x, 10**m2)
    high2, low2 = divmod(y, 10**m2)

    # Apply the algorithm
    z0 = multiplyKaratsuba(low1,low2)
    z1 = multiplyKaratsuba((low1+high1),(low2+high2))
    z2 = multiplyKaratsuba(high1,high2)

    return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)