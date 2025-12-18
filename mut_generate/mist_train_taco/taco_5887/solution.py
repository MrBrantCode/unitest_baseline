"""
QUESTION:
Chef has a natural number N. Cheffina challenges chef to check whether the given number is divisible by the sum of its digits or not. If the given number is divisible then print "Yes" else "No".

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains a single line of input, $N$. 

-----Output:-----
For each test case, output in a single line answer.

-----Constraints-----
- $1 \leq T \leq 10^6$
- $1 \leq N \leq 10^6$

-----Sample Input:-----
2
16
27

-----Sample Output:-----
No
Yes
"""

def is_divisible_by_sum_of_digits(N: int) -> str:
    """
    Checks if the given number N is divisible by the sum of its digits.

    Parameters:
    - N (int): The number to be checked.

    Returns:
    - str: "Yes" if N is divisible by the sum of its digits, otherwise "No".
    """
    # Calculate the sum of the digits of N
    sum_of_digits = sum(int(digit) for digit in str(N))
    
    # Check if N is divisible by the sum of its digits
    if N % sum_of_digits == 0:
        return "Yes"
    else:
        return "No"