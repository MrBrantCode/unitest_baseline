"""
QUESTION:
Write a function named `fibonacci_series` that takes a non-negative integer `n` as input and prints the first `n` Fibonacci numbers. The function should use matrix exponentiation and memoization techniques to achieve a time complexity of O(Log n). The function should also handle edge cases where `n` is 0 or a negative integer.
"""

def fibonacci_series(n):
  def multiply(F, M): 
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0] 
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1] 
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0] 
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]

    F[0][0] = x 
    F[0][1] = y 
    F[1][0] = z 
    F[1][1] = w 

  def power(F, n):
    if n == 0 or n == 1:
      return
    M = [[1, 1], [1, 0]] 

    power(F, n // 2)
    multiply(F, F)
    if n % 2 != 0:
      multiply(F, M)

  def fib(n):
    F = [[1, 1], [1, 0]] 
    if n == 0: 
      return 0
    power(F, n - 1)
    return F[0][0]

  if n < 0:
    print("Invalid input, please enter non-negative integer.")
  else:
    for i in range(n):
      print(fib(i), end=" ")