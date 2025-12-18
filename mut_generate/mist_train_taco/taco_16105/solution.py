"""
QUESTION:
You are given an array A, consisting of N distinct integers.  
Calculate number of pairs (i,j) (1 ≤ i < j ≤ N), such that 2 \cdot (A_{i} \oplus A_{j}) = A_{i} + A_{j}, where \oplus denotes [bitwise XOR].

------ Input Format ------ 

- The first line contains two integers N - the size of the array. 
- The second line contains N space-separated integers A_{1}, \ldots, A_{N} - the elements of the array A.

------ Output Format ------ 

For each test case, output the number of pairs satisfying constraints.

------ Constraints ------ 

$2 ≤ N ≤ 10^{6}$
$1 ≤ A_{i} ≤ 2^{60}-1$

------ subtasks ------ 

Subtask $1$ (20 points): $2 ≤ N ≤ 2000$
Subtask $2$ (40 points): $1 ≤ A_{i} ≤ 2^{20}-1$
Subtask $3$ (40 points): Original constraints.

----- Sample Input 1 ------ 
4
1 2 3 6

----- Sample Output 1 ------ 
2

----- explanation 1 ------ 
There are $2$ pairs $(i,j)$ satisfying all the conditions.
- $(i,j)= (1, 3)$. Thus, $2\cdot (A_{1}\oplus A_{3}) = 2\cdot (1\oplus 3) = 2\cdot 2 = 4$. Also, $A_{1}+A_{3} = 1+3 = 4$.
- $(i,j)= (2, 4)$. Thus, $2\cdot (A_{2}\oplus A_{4}) = 2\cdot (2\oplus 6) = 2\cdot 4 = 8$. Also, $A_{2}+A_{4} = 2+6 = 8$.

----- Sample Input 2 ------ 
5
4 3 9 7 1
----- Sample Output 2 ------ 
1
----- explanation 2 ------ 
There is only one pair $(i,j)$ satisfying all the conditions:
- $(i,j) = (2, 5)$. Thus, $2\cdot (A_{2}\oplus A_{5}) = 2\cdot (3\oplus 1) = 2\cdot 2 = 4$. Also, $A_{2}+A_{5} = 3+1 = 4$.
"""

def count_valid_pairs(arr):
    def patt(n):
        s = format(n, 'b')[1:]
        i = len(s) - 1
        while i >= 0:
            if s[i] == '1':
                if i - 1 < 0:
                    return False
                i -= 2
            else:
                i -= 1
        return True

    def rev(n):
        s = format(n, 'b')[1:]
        ans = ''
        i = len(s) - 1
        while i >= 0:
            if s[i] == '1':
                if s[i - 1] == '1':
                    ans = '01' + ans
                else:
                    ans = '11' + ans
                i -= 2
            else:
                ans = '0' + ans
                i -= 1
        ans = '11' + ans
        return int(ans, 2)

    arr.sort()
    mapp = {}
    ans = 0
    for i in range(len(arr) - 1, -1, -1):
        p = patt(arr[i])
        if p and rev(arr[i]) in mapp:
            ans += 1
        mapp[arr[i]] = True
    return ans