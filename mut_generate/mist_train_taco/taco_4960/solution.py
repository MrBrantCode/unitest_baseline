"""
QUESTION:
X and A are integers between 0 and 9 (inclusive).
If X is less than A, print 0; if X is not less than A, print 10.

-----Constraints-----
 - 0 \leq X, A \leq 9
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
X A

-----Output-----
If X is less than A, print 0; if X is not less than A, print 10.

-----Sample Input-----
3 5

-----Sample Output-----
0

3 is less than 5, so we should print 0.
"""

def compare_x_and_a(X: int, A: int) -> int:
    if X < A:
        return 0
    else:
        return 10