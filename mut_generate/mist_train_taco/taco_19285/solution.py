"""
QUESTION:
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.

 
Example 1:
Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.


Example 2:
Input: A = 4, B = 1
Output: "aabaa"
 

Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
"""

def generate_string_without_3a3b(A: int, B: int) -> str:
    if A >= 2 * B:
        return 'aab' * B + 'a' * (A - 2 * B)
    elif A >= B:
        return 'aab' * (A - B) + 'ab' * (2 * B - A)
    elif B >= 2 * A:
        return 'bba' * A + 'b' * (B - 2 * A)
    else:
        return 'bba' * (B - A) + 'ab' * (2 * A - B)