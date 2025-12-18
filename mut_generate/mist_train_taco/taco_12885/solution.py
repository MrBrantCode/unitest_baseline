"""
QUESTION:
There is an apple tree that bears apples of N colors. The N colors of these apples are numbered 1 to N, and there are a_i apples of Color i.

You and Lunlun the dachshund alternately perform the following operation (starting from you):

* Choose one or more apples from the tree and eat them. Here, the apples chosen at the same time must all have different colors.



The one who eats the last apple from the tree will be declared winner. If both you and Lunlun play optimally, which will win?

Constraints

* 1 \leq N \leq 10^5
* 1 \leq a_i \leq 10^9
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
a_1
a_2
:
a_N


Output

If you will win, print `first`; if Lunlun will win, print `second`.

Examples

Input

2
1
2


Output

first


Input

3
100000
30000
20000


Output

second
"""

def determine_winner(N, A):
    for a in A:
        if a % 2 != 0:
            return 'first'
    return 'second'