"""
QUESTION:
n children are standing in a circle and playing a game. Children's numbers in clockwise order form a permutation a_1, a_2, ..., a_{n} of length n. It is an integer sequence such that each integer from 1 to n appears exactly once in it.

The game consists of m steps. On each step the current leader with index i counts out a_{i} people in clockwise order, starting from the next person. The last one to be pointed at by the leader becomes the new leader.

You are given numbers l_1, l_2, ..., l_{m} — indices of leaders in the beginning of each step. Child with number l_1 is the first leader in the game. 

Write a program which will restore a possible permutation a_1, a_2, ..., a_{n}. If there are multiple solutions then print any of them. If there is no solution then print -1.


-----Input-----

The first line contains two integer numbers n, m (1 ≤ n, m ≤ 100).

The second line contains m integer numbers l_1, l_2, ..., l_{m} (1 ≤ l_{i} ≤ n) — indices of leaders in the beginning of each step.


-----Output-----

Print such permutation of n numbers a_1, a_2, ..., a_{n} that leaders in the game will be exactly l_1, l_2, ..., l_{m} if all the rules are followed. If there are multiple solutions print any of them. 

If there is no permutation which satisfies all described conditions print -1.


-----Examples-----
Input
4 5
2 3 1 4 4

Output
3 1 2 4 

Input
3 3
3 1 2

Output
-1



-----Note-----

Let's follow leadership in the first example:   Child 2 starts.  Leadership goes from 2 to 2 + a_2 = 3.  Leadership goes from 3 to 3 + a_3 = 5. As it's greater than 4, it's going in a circle to 1.  Leadership goes from 1 to 1 + a_1 = 4.  Leadership goes from 4 to 4 + a_4 = 8. Thus in circle it still remains at 4.
"""

def restore_permutation(n, m, leaders):
    a = [0] * (n + 1)
    
    def fail():
        return -1
    
    for i in range(m - 1):
        pr = -1
        if a[leaders[i]]:
            pr = a[leaders[i]]
        a[leaders[i]] = (leaders[i + 1] - leaders[i]) % n
        if a[leaders[i]] == 0:
            a[leaders[i]] = n
        if pr != -1 and pr != a[leaders[i]]:
            return fail()
    
    s = set(a)
    mex = 0
    for i in range(1, n + 1):
        if not a[i]:
            while mex in s:
                mex += 1
            a[i] = mex
            s.add(mex)
    
    if sorted(a[1:]) != list(range(1, n + 1)):
        return fail()
    
    return a[1:]