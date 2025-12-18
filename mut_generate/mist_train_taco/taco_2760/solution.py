"""
QUESTION:
Takahashi, Aoki and Snuke love cookies. They have A, B and C cookies, respectively. Now, they will exchange those cookies by repeating the action below:

* Each person simultaneously divides his cookies in half and gives one half to each of the other two persons.



This action will be repeated until there is a person with odd number of cookies in hand.

How many times will they repeat this action? Note that the answer may not be finite.

Constraints

* 1 ≤ A,B,C ≤ 10^9

Input

Input is given from Standard Input in the following format:


A B C


Output

Print the number of times the action will be performed by the three people, if this number is finite. If it is infinite, print `-1` instead.

Examples

Input

4 12 20


Output

3


Input

14 14 14


Output

-1


Input

454 414 444


Output

1
"""

def count_cookie_exchange_iterations(A, B, C):
    if A == B == C:
        return 0 if A % 2 else -1
    
    cnt = 0
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        A, B, C = (B + C) // 2, (C + A) // 2, (A + B) // 2
        cnt += 1
    
    return cnt