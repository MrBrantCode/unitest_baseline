"""
QUESTION:
Create a function named `calculate_fibonacci(n)` that takes a positive integer `n` as input and returns the `n`th Fibonacci number. The function should return 0 for `n = 1`, 1 for `n = 2`, and the sum of the two preceding numbers for `n > 2`. If `n` is less than or equal to 0, the function should print an error message.
"""

def calculate_fibonacci(n):
   if n <= 0:
       print("Input should be positive integer.")
   elif n == 1:
       return 0
   elif n == 2:
       return 1
   else:
       nth_fibo = [0, 1]
       for i in range(2, n):
           nth_fibo.append(nth_fibo[i-1] + nth_fibo[i-2])
       return nth_fibo[-1]