"""
QUESTION:
For an array A of N integers, define 

* An array P of length N, where P_{i} is the number of distinct elements in the subarray A[1:i] of A. 
* An array S of length N, where S_{i} is the number of distinct elements in the subarray A[i:N] of A. 

You are given arrays P and S. Determine whether there exists an array A corresponding to the given P and S arrays.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of the test cases follows.
- Each test case consists of three lines of input.
- The first line of each test case contains a single integer N.
- The second line of each test case contains N space-separated integers P_{1}, P_{2} \ldots P_{N}.
- The third line of each test case contains N space-separated integers S_{1}, S_{2} \ldots S_{N}.

------ Output Format ------ 

For each test case, output the answer on a new line: if there does not exist any array A producing such P and S arrays, then output NO, otherwise output YES 

You can output each letter in any case.

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$1 ≤ N ≤ 10^{5}$
$1 ≤ P_{i} ≤ N$
$1 ≤ S_{i} ≤ N$
- The sum of $N$ over all test cases doesn't exceed $2\cdot 10^{5}$

----- Sample Input 1 ------ 
4
3
1 2 3
3 2 1
4
2 2 3 3
3 2 2 1
2
1 1
1 1
3
1 2 1
2 2 1

----- Sample Output 1 ------ 
YES
NO
YES
NO

----- explanation 1 ------ 
Test case $1$: We have $P = [1, 2, 3]$ and $S = [3, 2, 1]$.

Consider $A = [1, 2, 3]$.
- The number of distinct elements in the $1$st prefix $[1]$ is $1$.
- The number of distinct elements in the $2$nd prefix $[1,2]$ is $2$.
- The number of distinct elements in the $3$rd prefix $[1,2,3]$ is $3$.

and
- The number of distinct elements in the $1$st suffix $[1,2,3]$ is $3$.
- The number of distinct elements in the $2$nd suffix $[2,3]$ is $2$.
- The number of distinct elements in the $3$rd suffix $[3]$ is $1$.

Clearly $A$ produces the given $P$ and $S$.

Test case $2$: We have $P =[2,2,3,3]$ , $S =[3,2,2,1]$.

It can be proven that there does not exist any array $A$ which produces the given $P$ and $S$.

Test case $3$: We have $P =[1,1]$, $S =[1,1]$.

Consider $A = [7,7]$.
- The number of distinct elements in the $1$st prefix $[7]$ is $1$.
- The number of distinct elements in the $2$nd prefix $[7,7]$ is $1$.

and
- The number of distinct elements in the $1$st suffix $[7,7]$ is $1$.
- The number of distinct elements in the $2$nd suffix $[7]$ is $1$.

Clearly $A$ produces the given $P$ and $S$.

Test case $4$: $P = [1,2,1]$ , $S =[2,2,1]$.

It can be proven that there does not exist any array $A$ which produces the given $P$ and $S$.
"""

def check_valid_array_existence(T, test_cases):
    results = []
    
    for case in test_cases:
        N, P, S = case
        ans = 'YES' if P[-1] == S[0] else 'NO'
        
        for i in range(N):
            if i == 0 and P[i] != 1 or (i > 0 and P[i] not in [P[i - 1], P[i - 1] + 1]):
                ans = 'NO'
                break
        
        if ans == 'NO':
            results.append(ans)
            continue
        
        for i in range(N)[::-1]:
            if i == N - 1 and S[i] != 1 or (i < N - 1 and S[i] not in [S[i + 1], S[i + 1] + 1]):
                ans = 'NO'
                break
        
        if ans == 'NO':
            results.append(ans)
            continue
        
        st = []
        for i in range(N):
            a = P[i] - (P[i - 1] if i - 1 >= 0 else 0)
            b = S[i] - (S[i + 1] if i + 1 < N else 0)
            
            if a and (not b):
                st.append('(')
            elif b and (not a):
                if st:
                    st.pop()
                else:
                    ans = 'NO'
                    break
            elif not b and (not a):
                if not st:
                    ans = 'NO'
                    break
        
        results.append(ans)
    
    return results