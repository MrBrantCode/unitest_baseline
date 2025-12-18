"""
QUESTION:
Create a recursive function called fibonacci(n1, n2) that prints all Fibonacci sequence numbers between 1 and 1000, where n1 and n2 are the last two numbers in the sequence. The function should start with n1 and n2 both equal to 1. It should stop recursing when the generated number exceeds 1000.
"""

def fibonacci(n1, n2):
    if n1 > 1000:
        return
    else:
        print(n1)
        fibonacci(n2, n1+n2)