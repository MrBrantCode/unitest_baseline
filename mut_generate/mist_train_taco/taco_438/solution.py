"""
QUESTION:
You are given integers A and B, each between 1 and 3 (inclusive).
Determine if there is an integer C between 1 and 3 (inclusive) such that A \times B \times C is an odd number.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq A, B \leq 3

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
If there is an integer C between 1 and 3 that satisfies the condition, print Yes; otherwise, print No.

-----Sample Input-----
3 1

-----Sample Output-----
Yes

Let C = 3. Then, A \times B \times C = 3 \times 1 \times 3 = 9, which is an odd number.
"""

def is_product_odd_possible(A: int, B: int) -> str:
    for C in range(1, 4):
        if A * B * C % 2 == 1:
            return 'Yes'
    return 'No'