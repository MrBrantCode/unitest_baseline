"""
QUESTION:
D: Is greed the best?

story

In Japan, where there are 1, 5, 10, 50, 100, 500 yen coins, it is known that the number of coins can be minimized by using as many coins as possible when paying a certain amount. ..

If the amount of coins is different from that of Japan, it is not always possible to minimize it by paying greedily.

What are the conditions that the amount of coins must meet in order to be optimally paid greedily?

problem

TAB was curious about the above, so I decided to first consider the case where there are only three types of coins, 1, A and B.

Since A and B are given, output the smallest amount of money that will not minimize the number of sheets if you pay greedily.

Also, if the greedy algorithm is optimal for any amount of money, output -1.

Input format


A B

Constraint

* 1 <A \ leq 10 ^ 5
* A <B \ leq 10 ^ 9



Input example 1


4 6

Output example 1


8

If you greedily pay 8 yen, you will pay 6 + 1 \ times 2 for a total of 3 cards, but you can pay 4 \ times 2 for a total of 2 cards.

Input example 2


2 1000000000

Output example 2


-1

It is best to greedily pay any amount.





Example

Input

4 6


Output

8
"""

def find_non_greedy_amount(A, B):
    if A > B:
        A, B = B, A
    
    if B % A == 0:
        return -1
    
    for i in range((B // A + 1) * A, B + A * 2, A):
        if i // A < i // B + (i - i // B * B) // A + (i - i // B * B) % A:
            return i
    
    return -1