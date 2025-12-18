"""
QUESTION:
Implement the Schönhage-Strassen function, which takes two lists of integers a and b as input, representing the coefficients of two polynomials, and returns the coefficients of their product. The function should use the Fast Fourier Transform to achieve a time complexity of O(n log n), where n is the degree of the polynomial.
"""

import cmath

def FFT_poly(a, n, w):
  if n == 1:
    return a
  a_even, a_odd = a[::2], a[1::2]
  half = n // 2
  w_sq = w * w
  y_even = FFT_poly(a_even, half, w_sq)
  y_odd = FFT_poly(a_odd, half, w_sq)
  y = [0] * n
  w_i = 1
  for i in range(half):
    y[i] = y_even[i] + w_i * y_odd[i]
    y[i + half] = y_even[i] - w_i * y_odd[i]
    w_i *= w
  return y

def Schonhage_Strassen(a, b):
  n = 1 << (len(a) + len(b) - 2).bit_length()
  w = cmath.exp(2j * cmath.pi / n)
  a += [0] * (n - len(a))
  b += [0] * (n - len(b))
  y_a = FFT_poly(a, n, w)
  y_b = FFT_poly(b, n, w)
  y_c = [y_ai * y_bi for y_ai, y_bi in zip(y_a, y_b)]
  c = FFT_poly(y_c, n, w**-1)
  c = [round(abs(x) / n) for x in c]
  while len(c) > 1 and c[-1] == 0:
    c.pop()
  return c