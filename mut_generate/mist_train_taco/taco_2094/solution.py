"""
QUESTION:
Given a natural number N, find the count of numbers from 1 to N that have an odd number of divisors.  
 
Example 1:
Input:
N = 1
Output:
1
Explanation:
1 has only one 
divisor {1}.
 
Example 2:
Input:
N = 4
Output:
2
Explanation:
4 has an odd number 
of divisors {1, 2, 4}.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function oddNumberOfDivisor() which takes an integer N and returns the count of numbers from 1 to n that have an odd number of divisors.  
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{6}
"""

def count_numbers_with_odd_divisors(N: int) -> int:
    """
    Counts the number of integers from 1 to N that have an odd number of divisors.

    Parameters:
    N (int): The upper limit of the range (1 to N) within which to count numbers.

    Returns:
    int: The count of numbers from 1 to N that have an odd number of divisors.
    """
    return int(N ** 0.5)