"""
QUESTION:
There are $n$ people in a row. The height of the $i$-th person is $a_i$. You can choose any subset of these people and try to arrange them into a balanced circle.

A balanced circle is such an order of people that the difference between heights of any adjacent people is no more than $1$. For example, let heights of chosen people be $[a_{i_1}, a_{i_2}, \dots, a_{i_k}]$, where $k$ is the number of people you choose. Then the condition $|a_{i_j} - a_{i_{j + 1}}| \le 1$ should be satisfied for all $j$ from $1$ to $k-1$ and the condition $|a_{i_1} - a_{i_k}| \le 1$ should be also satisfied. $|x|$ means the absolute value of $x$. It is obvious that the circle consisting of one person is balanced.

Your task is to choose the maximum number of people and construct a balanced circle consisting of all chosen people. It is obvious that the circle consisting of one person is balanced so the answer always exists.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of people.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 2 \cdot 10^5$), where $a_i$ is the height of the $i$-th person.


-----Output-----

In the first line of the output print $k$ — the number of people in the maximum balanced circle.

In the second line print $k$ integers $res_1, res_2, \dots, res_k$, where $res_j$ is the height of the $j$-th person in the maximum balanced circle. The condition $|res_{j} - res_{j + 1}| \le 1$ should be satisfied for all $j$ from $1$ to $k-1$ and the condition $|res_{1} - res_{k}| \le 1$ should be also satisfied.


-----Examples-----
Input
7
4 3 5 1 2 2 1

Output
5
2 1 1 2 3

Input
5
3 7 5 1 5

Output
2
5 5 

Input
3
5 1 4

Output
2
4 5 

Input
7
2 2 3 2 1 2 2

Output
7
1 2 2 2 2 3 2
"""

def find_max_balanced_circle(heights):
    n = len(heights)
    x = sorted(heights)
    ml = -1
    _i = 0
    _j = 0
    j = 0
    
    for i in range(n):
        j = max(j, i)
        while j + 1 < n and x[j + 1] == x[i]:
            j += 1
        while j + 2 < n and x[j + 2] == x[j] + 1:
            j += 2
            while j + 1 < n and x[j + 1] == x[j]:
                j += 1
        jj = j
        if j + 1 < n and x[j + 1] == x[j] + 1:
            jj += 1
        if jj - i > ml:
            ml = jj - i
            _i = i
            _j = jj
    
    a = []
    b = []
    i = _i
    while i <= _j:
        a.append(x[i])
        i += 1
        while i <= _j and x[i] == a[-1]:
            b.append(x[i])
            i += 1
    
    max_length = ml + 1
    balanced_circle = a + b[::-1]
    
    return max_length, balanced_circle