"""
QUESTION:
You are given three strings A, B and C. Check whether they form a word chain.
More formally, determine whether both of the following are true:
 - The last character in A and the initial character in B are the same.
 - The last character in B and the initial character in C are the same.
If both are true, print YES. Otherwise, print NO.

-----Constraints-----
 - A, B and C are all composed of lowercase English letters (a - z).
 - 1 ≤ |A|, |B|, |C| ≤ 10, where |A|, |B| and |C| are the lengths of A, B and C, respectively.

-----Input-----
Input is given from Standard Input in the following format:
A B C

-----Output-----
Print YES or NO.

-----Sample Input-----
rng gorilla apple

-----Sample Output-----
YES

They form a word chain.
"""

def is_word_chain(A: str, B: str, C: str) -> str:
    if A[-1] == B[0] and B[-1] == C[0]:
        return 'YES'
    else:
        return 'NO'