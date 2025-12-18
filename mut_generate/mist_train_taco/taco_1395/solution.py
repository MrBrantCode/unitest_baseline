"""
QUESTION:
Read problems statements in Mandarin Chinese here 

------ Problem Statement ------ 

Little Elephant from Zoo of Lviv likes bamboo very much. He currently has n stems of bamboo, H_{i} - height of i-th stem of bamboo (0-based numeration). 

Today inspector Andrii from World Bamboo Association is visiting the plantation. He doesn't like current situation. He wants the height of i-th stem to be D_{i}, for each i from 0 to n-1, inclusive.

Little Elephant is going to buy some special substance. One bottle of such substance he can use to single stem of bamboo. After using substance for stem i, the height of i-th stem is decrased by 1 and the height of j-th stem is increased by 1 for each j not equal to i. Note that it is possible for some of the stems to have negative height, but after all transformations all stems should have positive height.

Substance is very expensive. Help Little Elephant and find the minimal number of bottles of substance required for changing current plantation to one that inspector wants. If it's impossible, print -1.

------ Input ------ 

First line contain single integer T - the number of test cases. T test cases follow. First line of each test case contains single integer n - the number of stems in the plantation. Second line contains n integers separated by single space - starting plantation. Next line of each test case contains n integers - plantation that inspector Andrii requires.

------ Output ------ 

In T lines print T integers - the answers for the corresponding test cases.

------ Constraints ------ 

1 ≤ T ≤ 50

1 ≤ n ≤ 50

1 ≤ H_{i}, D_{i} ≤ 50

----- Sample Input 1 ------ 
3
1
1
2
2
1 2
2 1
3
3 2 2
4 5 3
----- Sample Output 1 ------ 
-1
1
5
"""

def calculate_min_bottles(n, H, D):
    if n == 1:
        return max(H[0] - D[0], -1)
    elif n == 2:
        a = H[0] - D[0]
        b = H[1] - D[1]
        if a == 0 and b == 0:
            return 0
        elif a != b and abs(a) == abs(b):
            return abs(a)
        else:
            return -1
    else:
        d = sum(D)
        h = sum(H)
        if d < h:
            return -1
        r = (d - h) % (n - 2)
        if r != 0:
            return -1
        s = (d - h) // (n - 2)
        for i in range(n):
            r = (s + H[i] - D[i]) % 2
            if r != 0:
                return -1
            xi = 0.5 * (s + H[i] - D[i])
            if xi < 0:
                return -1
        return int(s)