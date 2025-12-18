"""
QUESTION:
Create a function named `factorial` that calculates the factorial of an integer `n`. The function should handle both non-negative and negative integers, but since the factorial is not defined for negative integers, it should return a specific value for negative inputs. The function should be efficient and handle a wide range of integer inputs. The implementation should be consistent with the known factorial function for non-negative integers (i.e., n! = n*(n-1)*(n-2)*...*3*2*1 for n>=0).
"""

def factorial(n):
    """
    Calculates the factorial of an integer (n ≥ 0) and returns None for negative values.
    The factorial function is not defined for negative integers. Instead of returning an error or exception, 
    this function returns None and prints out a message.
    The function proves to be internally consistent with the known factorial function for non-negative integers 
    (i.e., n! = n*(n-1)*(n-2)*...*3*2*1 for n≥0).
    """
    if n < 0:
        print("The factorial function isn’t defined for negative integers")
        return None
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact