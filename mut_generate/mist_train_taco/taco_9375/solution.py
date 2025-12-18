"""
QUESTION:
For a given non-negative integer N, find the next smallest Happy Number. A number is called happy if it leads to 1 after a sequence of steps. Wherein at each step the number is replaced by the sum of squares of its digits that is if we start with Happy Number and keep replacing it with sum of squares of its digits, we reach 1 at some point. 
 
Example 1:
Input:
N = 8
Output:
10
Explanation:
Next happy number after 8 is 10 since
1*1 + 0*0 = 1
Example 2:
Input:
N = 10
Output
13
Explanation:
After 10, 13 is the smallest happy number because
1*1 + 3*3 = 10, so we replace 13 by 10 and 1*1 + 0*0 = 1.
Your Task:
You don't need to read input or print anything. Your task is to complete the function nextHappy() which takes an integer N as input parameters and returns an integer, next Happy number after N.
Expected Time Complexity: O(Nlog_{10}N)
Expected Space Complexity: O(1)
 
Constraints:
1<=N<=10^{5}
"""

def sum_of_squares(n):
    """Helper function to calculate the sum of squares of digits of a number."""
    summ = 0
    while n != 0:
        dg = n % 10
        summ += dg * dg
        n //= 10
    return summ

def is_happy_number(n):
    """Helper function to determine if a number is a happy number."""
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum_of_squares(n)
    return True

def find_next_happy_number(N):
    """Function to find the next happy number after N."""
    for i in range(N + 1, N + 100):
        if is_happy_number(i):
            return i
    return -1  # This line should theoretically never be reached due to constraints.