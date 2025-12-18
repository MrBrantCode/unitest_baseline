"""
QUESTION:
Given a positive integer N. You have to find N^{th} natural number after removing all the numbers containing digit 9.
Example 1:
Input:
N = 8
Output:
8
Explanation:
After removing natural numbers which contains
digit 9, first 8 numbers are 1,2,3,4,5,6,7,8
and 8^{th} number is 8.
Example 2:
Input:
N = 9
Output:
10
Explanation:
After removing natural numbers which contains
digit 9, first 9 numbers are 1,2,3,4,5,6,7,8,10
and 9^{th} number is 10.
 
Your Task:
You don't need to read input or print anything. Complete the function findNth() which accepts an integer N as input parameter and return the N^{th} number after removing all the numbers containing digit 9.
Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{12}
"""

def find_nth_natural_number_without_9(N: int) -> int:
    res, P = 0, 1
    while N > 0:
        res += P * (N % 9)
        N = N // 9
        P *= 10
    return res