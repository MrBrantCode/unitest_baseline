"""
QUESTION:
Write a function `multiply` that takes two large numbers `x` and `y` and returns their product using the divide and conquer strategy. The function should divide the numbers into two halves, compute the products of the halves recursively, and combine the results to obtain the final product. Assume the numbers can be divided into two halves of approximately equal size, represented as `a*2^n/2 + b` and `c*2^n/2 + d`.
"""

def multiply(x, y):
  threshold = 10
  n = max(len(str(x)), len(str(y)))
  if n < threshold:
    return x * y
  else:
    m = n // 2
    a = x // (2 ** m)
    b = x % (2 ** m)
    c = y // (2 ** m)
    d = y % (2 ** m)
    ac = multiply(a, c)
    bd = multiply(b, d)
    ad_bc = multiply(a + b, c + d) - ac - bd
    return ac * (2 ** (2 * m)) + ad_bc * (2 ** m) + bd