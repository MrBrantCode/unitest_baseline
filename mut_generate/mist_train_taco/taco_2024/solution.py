"""
QUESTION:
In the beginning, Takahashi has A cookies, and Aoki has B cookies. They will perform the following operation alternately, starting from Takahashi:

* If the number of cookies in his hand is odd, eat one of those cookies; if the number is even, do nothing. Then, give one-half of the cookies in his hand to the other person.



Find the numbers of cookies Takahashi and Aoki respectively have after performing K operations in total.

Constraints

* 1 \leq A,B \leq 10^9
* 1 \leq K \leq 100
* A,B and K are integers.

Input

Input is given from Standard Input in the following format:


A B K


Output

Print the number of cookies Takahashi has, and the number of cookies Aoki has, in this order, after performing K operations in total.

Examples

Input

5 4 2


Output

5 3


Input

3 3 3


Output

1 3


Input

314159265 358979323 84


Output

448759046 224379523
"""

def simulate_cookie_operations(A: int, B: int, K: int) -> tuple:
    for i in range(K):
        if i % 2 == 0:
            # Takahashi's turn
            if A % 2 == 1:
                A -= 1
            half_A = A // 2
            A -= half_A
            B += half_A
        else:
            # Aoki's turn
            if B % 2 == 1:
                B -= 1
            half_B = B // 2
            B -= half_B
            A += half_B
    return (A, B)