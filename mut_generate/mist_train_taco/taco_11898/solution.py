"""
QUESTION:
A permutation of length $n$ is an array $p=[p_1,p_2,\dots, p_n]$ which contains every integer from $1$ to $n$ (inclusive) exactly once. For example, $p=[4, 2, 6, 5, 3, 1]$ is a permutation of length $6$.

You are given three integers $n$, $a$ and $b$, where $n$ is an even number. Print any permutation of length $n$ that the minimum among all its elements of the left half equals $a$ and the maximum among all its elements of the right half equals $b$. Print -1 if no such permutation exists.


-----Input-----

The first line of the input contains one integer $t$ ($1 \le t \le 1000$), the number of test cases in the test. The following $t$ lines contain test case descriptions.

Each test case description contains three integers $n$, $a$, $b$ ($2 \le n \le 100$; $1 \le a,b \le n$; $a \ne b$), where $n$ is an even number (i.e. $n mod 2 = 0$).


-----Output-----

For each test case, print a single line containing any suitable permutation. Print -1 no such permutation exists. If there are multiple answers, print any of them.


-----Examples-----

Input
7
6 2 5
6 1 3
6 4 3
4 2 4
10 5 3
2 1 2
2 2 1
Output
4 2 6 5 3 1
-1
6 4 5 1 3 2 
3 2 4 1 
-1
1 2 
2 1


-----Note-----

None
"""

def find_permutation(n, a, b):
    half_len = n // 2
    arr_a = []
    arr_b = []
    len_a = -1
    len_b = -1
    
    if a < b:
        arr_a = [a] + list(range(b + 1, n + 1))
        len_a = n - b + 1
        arr_b = [b] + list(range(1, a))
        len_b = a
        if len_a <= half_len and len_b <= half_len:
            arr_a += list(range(a + 1, half_len - len_a + a + 1))
            arr_b += list(range(half_len - len_a + a + 1, b))
        else:
            len_a = -1
            len_b = -1
    elif a == half_len + 1 and b == half_len:
        len_b = half_len
        len_a = half_len
        arr_b += list(range(1, b + 1))
        arr_a += list(range(a, n + 1))
    
    if len_a == -1 and len_b == -1:
        return -1
    else:
        return arr_a + arr_b