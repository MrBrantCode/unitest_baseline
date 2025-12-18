"""
QUESTION:
You are given a table $a$ of size $2 \times n$ (i.e. two rows and $n$ columns) consisting of integers from $1$ to $n$.

In one move, you can choose some column $j$ ($1 \le j \le n$) and swap values $a_{1, j}$ and $a_{2, j}$ in it. Each column can be chosen no more than once.

Your task is to find the minimum number of moves required to obtain permutations of size $n$ in both first and second rows of the table or determine if it is impossible to do that.

You have to answer $t$ independent test cases.

Recall that the permutation of size $n$ is such an array of size $n$ that contains each integer from $1$ to $n$ exactly once (the order of elements doesn't matter).


-----Input-----

The first line of the input contains one integer $t$ ($1 \le t \le 2 \cdot 10^4$) — the number of test cases. Then $t$ test cases follow.

The first line of the test case contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of columns in the table. The second line of the test case contains $n$ integers $a_{1, 1}, a_{1, 2}, \dots, a_{1, n}$ ($1 \le a_{1, i} \le n$), where $a_{1, i}$ is the $i$-th element of the first row of the table. The third line of the test case contains $n$ integers $a_{2, 1}, a_{2, 2}, \dots, a_{2, n}$ ($1 \le a_{2, i} \le n$), where $a_{2, i}$ is the $i$-th element of the second row of the table.

It is guaranteed that the sum of $n$ does not exceed $2 \cdot 10^5$ ($\sum n \le 2 \cdot 10^5$).


-----Output-----

For each test case print the answer: -1 if it is impossible to obtain permutation of size $n$ in both first and the second rows of the table, or one integer $k$ in the first line, where $k$ is the minimum number of moves required to obtain permutations in both rows, and $k$ distinct integers $pos_1, pos_2, \dots, pos_k$ in the second line ($1 \le pos_i \le n$) in any order — indices of columns in which you need to swap values to obtain permutations in both rows. If there are several answers, you can print any.


-----Example-----
Input
6
4
1 2 3 4
2 3 1 4
5
5 3 5 1 4
1 2 3 2 4
3
1 2 1
3 3 2
4
1 2 2 1
3 4 3 4
4
4 3 1 4
3 2 2 1
3
1 1 2
3 2 2

Output
0

2
2 3 
1
1 
2
3 4 
2
3 4 
-1
"""

def find_min_moves_for_permutations(n, row1, row2):
    pos = [[] for _ in range(n + 1)]
    for i in range(n):
        pos[row1[i]].extend((i, 0))
        pos[row2[i]].extend((i, 1))
        if len(pos[row1[i]]) > 4 or len(pos[row2[i]]) > 4:
            return -1, []
    
    was = [False] * (n + 1)
    res = []
    
    for i in range(1, n + 1):
        if not was[i]:
            x = i
            p = pos[i][0]
            if pos[i][1] == 1:
                (one, two) = ([p], [])
            else:
                (one, two) = ([], [p])
            first = p
            while True:
                was[x] = True
                if pos[x][0] == p:
                    p = pos[x][2]
                    if p == first:
                        break
                    r = pos[x][3]
                else:
                    p = pos[x][0]
                    if p == first:
                        break
                    r = pos[x][1]
                if r == 0:
                    one.append(p)
                    x = row2[p]
                else:
                    two.append(p)
                    x = row1[p]
            if len(one) > len(two):
                one = two
            res.extend(one)
    
    return len(res), [i + 1 for i in res]