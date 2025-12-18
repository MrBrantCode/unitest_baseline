"""
QUESTION:
Damon is a mathematician, and he calls a integer N Damon Prime if N+1 and N-1 both are prime numbers. He will give you an integer N, you need to find whether the number is Damon Prime or not.  
For example:  4 is a damon prime, 5 is not a damon prime, 102 is a damon prime, 9 is not a damon prime, etc . 
Example 1:
Input: N = 4
Output: "Yes" 
Explanation: According to Damon 4
is a Damon Prime.
Example 2:
Input: N = 5
Output: "No"
Explanation: According to Damon 5
is not a Damon Prime. 
Your Task:  
You dont need to read input or print anything. Complete the function damonPrime() which takes N as input parameter and returns "Yes" if N is a Damon Prime else return "No".
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
Constraints:
1<= N <=10^{4}
"""

from math import sqrt

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_damon_prime(N):
    """Function to check if N is a Damon Prime."""
    if is_prime(N - 1) and is_prime(N + 1):
        return "Yes"
    else:
        return "No"