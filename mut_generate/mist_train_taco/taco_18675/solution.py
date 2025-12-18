"""
QUESTION:
Polycarp plays "Game 23". Initially he has a number $n$ and his goal is to transform it to $m$. In one move, he can multiply $n$ by $2$ or multiply $n$ by $3$. He can perform any number of moves.

Print the number of moves needed to transform $n$ to $m$. Print -1 if it is impossible to do so.

It is easy to prove that any way to transform $n$ to $m$ contains the same number of moves (i.e. number of moves doesn't depend on the way of transformation).


-----Input-----

The only line of the input contains two integers $n$ and $m$ ($1 \le n \le m \le 5\cdot10^8$).


-----Output-----

Print the number of moves to transform $n$ to $m$, or -1 if there is no solution.


-----Examples-----
Input
120 51840

Output
7

Input
42 42

Output
0

Input
48 72

Output
-1



-----Note-----

In the first example, the possible sequence of moves is: $120 \rightarrow 240 \rightarrow 720 \rightarrow 1440 \rightarrow 4320 \rightarrow 12960 \rightarrow 25920 \rightarrow 51840.$ The are $7$ steps in total.

In the second example, no moves are needed. Thus, the answer is $0$.

In the third example, it is impossible to transform $48$ to $72$.
"""

def transform_number_moves(n: int, m: int) -> int:
    if m % n != 0:
        return -1
    
    res = 0
    a = m // n
    
    while a % 2 == 0:
        a //= 2
        res += 1
    
    while a % 3 == 0:
        a //= 3
        res += 1
    
    if a == 1:
        return res
    else:
        return -1