"""
QUESTION:
You are given three strings A, B and C. Each of these is a string of length N consisting of lowercase English letters.

Our objective is to make all these three strings equal. For that, you can repeatedly perform the following operation:

* Operation: Choose one of the strings A, B and C, and specify an integer i between 1 and N (inclusive). Change the i-th character from the beginning of the chosen string to some other lowercase English letter.



What is the minimum number of operations required to achieve the objective?

Constraints

* 1 \leq N \leq 100
* Each of the strings A, B and C is a string of length N.
* Each character in each of the strings A, B and C is a lowercase English letter.

Input

Input is given from Standard Input in the following format:


N
A
B
C


Output

Print the minimum number of operations required.

Examples

Input

4
west
east
wait


Output

3


Input

9
different
different
different


Output

0


Input

7
zenkoku
touitsu
program


Output

13
"""

def minimum_operations_to_equalize_strings(N, A, B, C):
    ans = 0
    for i in range(N):
        if A[i] == B[i] == C[i]:
            ans += 0
        elif A[i] == B[i] or B[i] == C[i] or C[i] == A[i]:
            ans += 1
        else:
            ans += 2
    return ans