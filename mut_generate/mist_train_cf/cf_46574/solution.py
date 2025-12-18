"""
QUESTION:
Write a function named `fibonacci(n)` that generates and returns the first n numbers in the Fibonacci sequence. The function should handle potential errors during execution, including invalid input values for `n`. The function should allow the user to specify the value of `n`. If `n` is not a positive integer, the function should handle the error and display an appropriate message.
"""

def fibonacci(n):
  try:
    if n<=0:
      print("Invalid input: The number should be greater than zero")
      return
    a, b = 0, 1
    fibonacci_sequence = [0, 1]

    for _ in range(2, n):
      a, b = b, a + b
      fibonacci_sequence.append(b)
      
    return fibonacci_sequence[:n]
  except Exception as e:
    print("An error occurred: ", str(e))