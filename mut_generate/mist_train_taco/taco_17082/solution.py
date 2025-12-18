"""
QUESTION:
Problem

You decide to play a weird game with your friend A, who loves gathering.

Given a set S of non-negative integers consisting of n elements that can be duplicated. Each element contained in the set S is a non-negative pi-ary number. With Steps 1 to 3 below as one turn for the set S, you and your opponent repeat the turn alternately. In each turn, operate in the order of this number.

Step 1: Remove all the elements contained in the set S once, convert each removed element to a binary number, erase 0, divide it into one or more consecutive 1s, and divide the divided part. Add all to set S.

Step 2: If Set S is empty at this time, the player currently playing this turn loses.
Step 3: Select one element a contained in the set S, and subtract any integer x that satisfies 1 ≤ x ≤ a from that a.


The figure below is an example of how to proceed for the first turn given the following inputs.


Four
10 3
2 11
16 5
16 AE


<image>


The first is your turn. When both parties do their best for a given input, do you really win?



Input

The input is given in the following format:


n
p1 m1
p2 m2
...
pi mi
...
pn mn


N pi-ary numbers mi, which are elements of the set, are given. The number n of elements in the set does not exceed 105. Also, 2 ≤ pi ≤ 62 is satisfied. The pi-ary number mi uses 52 letters of the alphabet in addition to the usual numbers 0-9. The order is 012 ... 789 ABC ... XYZabc ... xyz in ascending order, and the characters up to the i-th are used. Also, the pi-ary mi does not exceed 218-1 in decimal.

Output

Output win if you win against the given input, lose if you lose.

Examples

Input

1
10 1


Output

win


Input

2
10 1
10 1


Output

lose


Input

3
25 53AI
43 3BI0
62 pn6


Output

win
"""

def determine_game_outcome(n, elements):
    ans = 0
    for pi, mi in elements:
        s = 0
        for m in mi:
            if m.isdigit():
                s += int(m)
            elif m.isupper():
                s += ord(m) - ord('A') + 10
            else:
                s += ord(m) - ord('a') + 36
        ans ^= s
    return 'win' if ans else 'lose'