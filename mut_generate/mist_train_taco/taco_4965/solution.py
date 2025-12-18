"""
QUESTION:
A Fibonacci series (starting from 1) written in order without any spaces in between, thus producing a sequence of digits. Find the nth digit in the sequence.
Example 1:
Input: n = 3
Output: 2 
Explanation: 3rd digit of fibonacci 
series is 2(1123.....).
Example 2:
Input: n = 7
Output: 1
Explanation: 7th digit of fibonacci
series is 1(11235811.....).
Your Task:  
You dont need to read input or print anything. Complete the function nthFibonacciDigit() which takes n as input parameter and returns nth digit of fabonacci series. 
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n)
Constraints:
1<= n <=100
"""

def nth_fibonacci_digit(n: int) -> str:
    """
    Returns the nth digit in the Fibonacci sequence (starting from 1) written in order without any spaces in between.

    Parameters:
    n (int): The position of the digit in the Fibonacci sequence (1-based index).

    Returns:
    str: The nth digit in the Fibonacci sequence as a single character string.
    """
    if n < 1 or n > 100:
        raise ValueError("n must be between 1 and 100 inclusive.")
    
    # Generate the Fibonacci sequence digits
    a, b = 1, 1
    fib_digits = ['1', '1']
    for _ in range(98):  # Since we already have the first two digits
        c = a + b
        fib_digits.extend(list(str(c)))
        a, b = b, c
    
    # Return the nth digit (1-based index)
    return fib_digits[n - 1]