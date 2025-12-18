"""
QUESTION:
You are given four distinct integers $a$, $b$, $c$, $d$.

Timur and three other people are running a marathon. The value $a$ is the distance that Timur has run and $b$, $c$, $d$ correspond to the distances the other three participants ran.

Output the number of participants in front of Timur.


-----Input-----

The first line contains a single integer $t$ ($1 \leq t \leq 10^4$) — the number of test cases.

The description of each test case consists of four distinct integers $a$, $b$, $c$, $d$ ($0 \leq a, b, c, d \leq 10^4$).


-----Output-----

For each test case, output a single integer — the number of participants in front of Timur.


-----Examples-----

Input
4
2 3 4 1
10000 0 1 2
500 600 400 300
0 9999 10000 9998
Output
2
0
1
3


-----Note-----

For the first test case, there are $2$ people in front of Timur, specifically the participants who ran distances of $3$ and $4$. The other participant is not in front of Timur because he ran a shorter distance than Timur.

For the second test case, no one is in front of Timur, since he ran a distance of $10000$ while all others ran a distance of $0$, $1$, and $2$ respectively.

For the third test case, only the second person is in front of Timur, who ran a total distance of $600$ while Timur ran a distance of $500$.
"""

def count_participants_in_front(a, b, c, d):
    """
    Counts the number of participants who have run a greater distance than Timur.

    Parameters:
    a (int): The distance Timur has run.
    b (int): The distance the first participant has run.
    c (int): The distance the second participant has run.
    d (int): The distance the third participant has run.

    Returns:
    int: The number of participants who have run a greater distance than Timur.
    """
    return (b > a) + (c > a) + (d > a)