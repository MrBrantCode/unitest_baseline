"""
QUESTION:
You are given N integers A_{1}, A_{2}, \ldots, A_{N}. Find *any* permutation B_{1}, B_{2}, \ldots, B_{N} of these integers, for which the value of \min(|B_{1} - B_{2}|, |B_{2} - B_{3}|, \ldots, |B_{N} - B_{1}|) is maximized.

------ Input Format ------ 

- The first line of the input contains a single integer T, the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer N — the number of integers.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.

------ Output Format ------ 

For each test case, output N integers B_{1}, B_{2}, \ldots, B_{N} — the permutation of A_{1}, A_{2}, \ldots, A_{N} for which the value of \min(|B_{1} - B_{2}|, |B_{2} - B_{3}|, \ldots, |B_{N} - B_{1}|) is maximized.

If there are multiple such permutations, you can output any of them.

------ Constraints ------ 

$1 ≤T ≤10^{4}$
$3 ≤N ≤10^{5}$ 
$0 ≤A_{i} ≤10^{9}$
- The sum of $N$ over all test cases doesn't exceed $2\cdot 10^{5}$.

----- Sample Input 1 ------ 
4
5
0 10 0 10 0
4
1 5 10 14
4
1 6 10 15
5
1 2 3 4 5
----- Sample Output 1 ------ 
0 0 10 0 10 
1 10 5 14 
6 15 10 1 
1 3 5 2 4 
----- explanation 1 ------ 
Test case $1$: For $B = [0, 0, 10, 0, 10]$, the value of $\min(|B_{1} - B_{2}|, |B_{2} - B_{3}|, \ldots, |B_{N} - B_{1}|)$ is $0$. It can be shown that this is the maximum possible value. Other permutations also achieve this value, for example $[0, 10, 0, 10, 0]$, and any such permutation is a valid output.

Test case $2$: For $B = [1, 10, 5, 14]$, the value of $\min(|B_{1} - B_{2}|, |B_{2} - B_{3}|, \ldots, |B_{N} - B_{1}|)$ is $5$. It can be shown that this is the maximum possible.
"""

def maximize_min_difference(test_cases):
    def mine(ans):
        mi = float('inf')
        for i in range(1, len(ans)):
            temp = abs(ans[i] - ans[i - 1])
            if temp < mi:
                mi = temp
        return mi

    def swap(ans):
        mi = mine(ans)
        (l, b) = (-1, -1)
        for i in range(4):
            for j in range(i + 1, 3):
                temp = ans.copy()
                (temp[i], temp[j]) = (temp[j], temp[i])
                temp1 = mine(temp)
                if temp1 > mi:
                    a = i
                    b = j
                    mi = temp1
        if l != -1:
            (ans[l], ans[b]) = (ans[b], ans[l])

    results = []
    for n, a in test_cases:
        a.sort()
        ans = []
        d = n // 2
        if n % 2 == 0:
            pos = []
            for i in range(d):
                if i % 2 == 0:
                    pos.append(i)
                else:
                    pos.append(i + d)
            for i in range(d - 1, -1, -1):
                if i % 2 == 0:
                    pos.append(i + d)
                else:
                    pos.append(i)
            mi = float('inf')
            for i in range(n // 2 + 1):
                temp = a[i + d - 1] - a[i]
                if temp < mi:
                    mi = temp
                    x = i
            for i in range(n):
                ans.append(a[(pos[i] + x) % n])
        else:
            ans.append(a[0])
            ans.append(a[n // 2])
            ans.append(a[n - 1])
            for i in range(d - 1, 0, -1):
                ans.append(a[i])
                ans.append(a[i + n // 2])
        results.append(ans)
    return results