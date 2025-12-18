"""
QUESTION:
Implement the Karatsuba algorithm for polynomial multiplication, which takes two integers `x` and `y` as input and returns their product. The function should work for inputs with an odd number of digits and should not exceed a time complexity of O(n^log2(3)) arithmetic operations.

The function should be named `karatsuba(x, y)`, where `x` and `y` are integers. The function should handle the case where the input integers have a different number of digits.
"""

def karatsuba(x,y):
  n = max(len(str(x)), len(str(y)))

  if n == 1:
    return x*y

  n_2 = n // 2

  a = x // 10**(n_2)
  b = x % 10**(n_2)
  c = y // 10**(n_2)
  d = y % 10**(n_2)

  ac = karatsuba(a, c)
  bd = karatsuba(b, d)
  ad_bc = karatsuba(a+b, c+d) - ac - bd

  product = ac * 10**(2*n_2) + ad_bc * 10**n_2 + bd
  
  return product