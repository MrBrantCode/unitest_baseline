"""
QUESTION:
You are given a string S of length N consisting of lowercase English letters, and an integer K. Print the string obtained by replacing every character in S that differs from the K-th character of S, with `*`.

Constraints

* 1 \leq K \leq N\leq 10
* S is a string of length N consisting of lowercase English letters.
* N and K are integers.

Input

Input is given from Standard Input in the following format:


N
S
K


Output

Print the string obtained by replacing every character in S that differs from the K-th character of S, with `*`.

Examples

Input

5
error
2


Output

*rr*r


Input

6
eleven
5


Output

e*e*e*


Input

9
education
7


Output

******i**
"""

def replace_differing_characters(N: int, S: str, K: int) -> str:
    # Ensure K is within the valid range
    if not (1 <= K <= N):
        raise ValueError("K must be between 1 and N inclusive")
    
    # Get the K-th character (1-based index, so K-1 for 0-based index)
    k_th_char = S[K - 1]
    
    # Create the resulting string
    result = ''.join((s if s == k_th_char else '*' for s in S))
    
    return result