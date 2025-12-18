"""
QUESTION:
Consider a sequence of numbers composed of only digits 4 and 7 such as 4, 7, 44, 47, 74,...... 44744,.. etc. Given a number N, we need to find the value of the N-th element in the sequence.
Example 1:
Input:
N = 3
Output:
44
Explanation:
Value of the first term = 4
Value of the second term = 7
Value of the third term = 44
Example 2:
Input:
N = 5
Output:
74
Explanation:
Value of the first term = 4
Value of the second term = 7
Value of the third term = 44
Value of the fourth term = 47
Value of the fifth term = 74
Your Task:  
You don't need to read input or print anything. Your task is to complete the function NthTermOfSeries() which takes an integer N as an input parameter and returns the value of the Nth term of the sequence.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 1000
"""

def nth_term_of_series(N: int) -> int:
    if N <= 0:
        return 0
    if N % 2 == 1:
        return 10 * nth_term_of_series((N - 1) // 2) + 4
    return 10 * nth_term_of_series((N - 1) // 2) + 7