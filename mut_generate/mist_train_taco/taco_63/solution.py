"""
QUESTION:
Given 3 characters 'a', 'b', 'c'. Find the number of strings of length n that can be formed from these 3 characters. Given that : we can use ‘a’ as many times as we want, ‘b’ maximum once, and ‘c’ maximum twice.
 
Example 1:
Input: n = 2
Output: 8
Expalantion: There are total 8 possible
strings and these are: {aa, ab, ba, ac,
ca, bc, cb, cc}.
Example 2:
Input: n = 3
Output: 19
Explanation: There are total 19 possible
strings.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function no_ofString() which takes n as input parameter ans returns the no. of total possible strings than can be formed using characters 'a', 'b' and 'c' modulo 10^{9} + 7.
 
Expected Time Complexity: O(n)
Expected Space Compelxity: O(n)
 
Constraints:
1 <= n <= 100000
"""

def count_possible_strings(n: int) -> int:
    MOD = 10**9 + 7
    return (1 + n * 2 + n * (n * n - 1) // 2) % MOD