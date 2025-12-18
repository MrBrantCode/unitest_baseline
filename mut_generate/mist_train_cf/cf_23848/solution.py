"""
QUESTION:
Implement a function named `fibonacci(n)` that calculates the nth Fibonacci number using recursion. The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it, starting from 0 and 1. The function should handle invalid inputs by printing an error message for negative inputs. The function should return the nth Fibonacci number for non-negative integers n.
"""

def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)