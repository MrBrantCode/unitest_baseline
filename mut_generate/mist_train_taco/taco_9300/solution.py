"""
QUESTION:
Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that $13$ is better than $31$ and that $12$ is better than ${11}$.

Given an integer, $n$, can you find the divisor of $n$ that Kristin will consider to be the best?

Input Format

A single integer denoting $n$.

Constraints

$0<n\leq10^5$

Output Format

Print an integer denoting the best divisor of $n$.  

Sample Input 0
12

Sample Output 0
6

Explanation 0

The set of divisors of $12$ can be expressed as $\{1,2,3,4,6,12\}$. The divisor whose digits sum to the largest number is ${6}$ (which, having only one digit, sums to itself). Thus, we print ${6}$ as our answer.
"""

def sum_digits(n):
    """Helper function to calculate the sum of digits of a number."""
    return sum(map(int, list(str(n))))

def find_best_divisor(n):
    """
    Finds the best divisor of n based on Kristen's criteria.

    Parameters:
    n (int): The number for which to find the best divisor.

    Returns:
    int: The best divisor of n.
    """
    best = 1
    best_sum = 1
    
    for k in range(1, n + 1):
        if n % k == 0:
            the_sum = sum_digits(k)
            if the_sum > best_sum:
                best_sum = the_sum
                best = k
            elif the_sum == best_sum and k < best:
                best = k
    
    return best