"""
QUESTION:
You have been given a positive integer N. You need to find and print the Factorial  of this number. The Factorial of a positive integer N refers to the product of all number in the range from 1 to N. You can read more about the factorial of a number here.

Input Format:
The first and only line of the input contains a single integer N denoting the number whose factorial you need to find. 

Output Format
Output a single line denoting the factorial of the number N.

Constraints
 1 ≤ N ≤ 10   

SAMPLE INPUT
2

SAMPLE OUTPUT
2
"""

def calculate_factorial(N: int) -> int:
    """
    Calculate the factorial of a given positive integer N.

    Parameters:
    N (int): The positive integer whose factorial needs to be calculated.

    Returns:
    int: The factorial of the number N.
    """
    if N < 1 or N > 10:
        raise ValueError("N should be between 1 and 10 inclusive.")
    
    factorial = 1
    while N != 0:
        factorial *= N
        N -= 1
    
    return factorial