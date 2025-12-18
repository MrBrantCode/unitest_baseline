"""
QUESTION:
Write a function `Karatsuba(x, y)` to multiply two numbers using the Karatsuba algorithm. The function should take two integers `x` and `y` as input, and return their product. The Karatsuba algorithm should be implemented using a divide and conquer approach to reduce the multiplication of two n-digit numbers to at most n^log2(3) single digit multiplications. Note that the input numbers are not limited to binary multiples and the multiplication by a power of the base is assumed to be a relatively cheap operation.
"""

def Karatsuba(x, y):
  if x<10 or y<10:
    return x*y

  n = max(len(str(x)), len(str(y)))
  m = n//2

  a = x // 10**(m)
  b = x % 10**(m)
  c = y // 10**(m)
  d = y % 10**(m)

  ac = Karatsuba(a, c)
  bd = Karatsuba(b, d)
  ad_bc = Karatsuba(a+b, c+d) - ac - bd

  prod = ac * 10**(2*m) + (ad_bc * 10**m) + bd

  return prod