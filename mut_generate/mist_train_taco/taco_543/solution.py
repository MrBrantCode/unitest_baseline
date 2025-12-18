"""
QUESTION:
One day, Yuhao came across a problem about checking if some bracket sequences are correct bracket sequences.

A bracket sequence is any non-empty sequence of opening and closing parentheses. A bracket sequence is called a correct bracket sequence if it's possible to obtain a correct arithmetic expression by inserting characters "+" and "1" into this sequence. For example, the sequences "(())()", "()" and "(()(()))" are correct, while the bracket sequences ")(", "(()" and "(()))(" are not correct.

Yuhao found this problem too simple for him so he decided to make the problem harder. You are given many (not necessarily correct) bracket sequences. The task is to connect some of them into ordered pairs so that each bracket sequence occurs in at most one pair and the concatenation of the bracket sequences in each pair is a correct bracket sequence. The goal is to create as many pairs as possible.

This problem unfortunately turned out to be too difficult for Yuhao. Can you help him and solve it?


-----Input-----

The first line contains one integer $n$ ($1 \leq n \leq 10^5$) — the number of bracket sequences.

Each of the following $n$ lines contains one bracket sequence — a non-empty string which consists only of characters "(" and ")".

The sum of lengths of all bracket sequences in the input is at most $5 \cdot 10^5$.

Note that a bracket sequence may appear in the input multiple times. In this case, you can use each copy of the sequence separately. Also note that the order in which strings appear in the input doesn't matter.


-----Output-----

Print a single integer — the maximum number of pairs which can be made, adhering to the conditions in the statement.


-----Examples-----
Input
7
)())
)
((
((
(
)
)

Output
2

Input
4
(
((
(((
(())

Output
0

Input
2
(())
()

Output
1



-----Note-----

In the first example, it's optimal to construct two pairs: "((     )())" and "(     )".
"""

def max_bracket_pairs(bracket_sequences):
    parr = {}
    narr = {}
    zero = 0
    ans = 0
    
    for s in bracket_sequences:
        x = 0
        y = 0
        left = True
        right = True
        
        for j in range(len(s)):
            if s[j] == '(':
                x += 1
            else:
                x -= 1
            if x < 0:
                left = False
            
            if s[-1 * (j + 1)] == '(':
                y += 1
            else:
                y -= 1
            if y > 0:
                right = False
        
        if left and right and (x == 0):
            zero += 1
        elif left or right:
            if x > 0:
                parr[x] = parr.get(x, 0) + 1
            else:
                narr[x] = narr.get(x, 0) + 1
    
    ans += zero // 2
    
    for i in narr.keys():
        ans += min(narr[i], parr.get(-i, 0))
    
    return ans