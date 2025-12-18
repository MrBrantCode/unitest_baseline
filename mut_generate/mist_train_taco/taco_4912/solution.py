"""
QUESTION:
Chef likes problems related to learning new languages. He only knows first N letters of English alphabet. Also he explores all M-letter words formed by the characters he knows. Define cost for a given M-letter word S, cost(S) = P1, S1+P2, S2+...+PM, SM, where Pi, j is i, jth entry of matrix P. Sort all the words by descending cost, if costs are equal, sort them lexicographically. You need to find K-th M-letter word in Chef's order.

-----Input-----
First line contains three positive integer numbers N, M and K.
Next M lines contains N integers per line, denoting the matrix P.

-----Output-----
Output in a single line K-th M-letter in Chef's order.

-----Constraints-----
- 1 ≤ N ≤ 16 
- 1 ≤ M ≤ 10 
- 1 ≤ K ≤ NM
- 0 ≤ Pi, j ≤ 109

-----Subtasks-----
- Subtask #1: (20 points) 1 ≤ K ≤ 10000
- Subtask #2: (20 points) 1 ≤ M ≤ 5
- Subtask #3: (60 points) Original constraints

-----Example-----
Input:2 5 17
7 9
13 18
10 12
4 18
3 9

Output:aaaba
"""

def find_kth_word(n, m, k, p):
    def dfs(ind, m, n, k):
        if ind == m:
            return ['']
        else:
            temp = dfs(ind + 1, m, n, k)
            ans = []
            if len(temp) < k:
                for i in temp:
                    for j in range(97, 97 + n):
                        ans += [chr(j) + i]
            else:
                for i in temp:
                    ans += ['z' + i]
            return ans

    mr = []
    for inp in p:
        mc = inp[0]
        mi = 0
        for j in range(1, n):
            if mc < inp[j]:
                mc = inp[j]
                mi = j
        mr += [mi]

    ans = dfs(0, m, n, k)
    w = []
    for i in ans:
        cst = 0
        s = ''
        for j in range(m):
            if i[j] != 'z':
                s += i[j]
                cst += p[j][ord(i[j]) - 97]
            else:
                s += chr(mr[j] + 97)
        w += [(-cst, s)]
    w.sort()
    return w[k - 1][1]