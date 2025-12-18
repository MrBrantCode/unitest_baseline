"""
QUESTION:
Given and integer N.Calculate the sum of series 1^{3} + 2^{3} + 3^{3} + 4^{3} + … till N-th term.
Example 1:
Input:
N=5
Output:
225
Explanation:
1^{3}+2^{3}+3^{3}+4^{3}+5^{3}=225
Example 2:
Input:
N=7
Output:
784
Explanation:
1^{3}+2^{3}+3^{3}+4^{3}+5^{3}+6^{3}+7^{3}=784
Your Task:
You don't need to read input or print anything.Your task is to complete the function sumOfSeries() which takes the integer N as parameter and returns the sum of the cubes of the first N natural numbers.
Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)
Constraints:
1<=N<=50000
"""

def sum_of_cubes(N: int) -> int:
    """
    Calculate the sum of the series 1^3 + 2^3 + 3^3 + ... + N^3.

    Parameters:
    N (int): The number of terms in the series.

    Returns:
    int: The sum of the cubes of the first N natural numbers.
    """
    return N ** 2 * (N + 1) ** 2 // 4