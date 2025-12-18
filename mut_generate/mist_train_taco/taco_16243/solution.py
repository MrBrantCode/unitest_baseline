"""
QUESTION:
Given a natural number n, calculate sum of all its proper divisors. A proper divisor of a natural number is the divisor that is strictly less than the number.
Example 1:
Input: n = 10
Output: 8 
Explanation: Proper divisors 1 + 2 + 5 = 8. 
Example 2:
Input: n = 6
Output: 6
Explanation: Proper divisors 1 + 2 + 3 = 6. 
Your Task:  
You dont need to read input or print anything. Complete the function divSum() which takes n as input parameter and returns sum of proper divisors of n.
Expected Time Complexity: O(sqrt(n))
Expected Auxiliary Space: O(1)
Constraints:
2<= n <=10^{6}
"""

import math

def sum_of_proper_divisors(n: int) -> int:
    """
    Calculate the sum of all proper divisors of a given natural number n.

    Parameters:
    n (int): The natural number for which to calculate the sum of proper divisors.

    Returns:
    int: The sum of all proper divisors of n.
    """
    s = 1  # Start with 1 because 1 is a proper divisor for any n > 1
    a = int(math.sqrt(n))
    for i in range(2, a + 1):
        if n % i == 0:
            if i * i == n:
                s += i  # Add only i if i is the square root of n
            else:
                b = n // i
                s += i + b  # Add both i and b if they are proper divisors
    return s