"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Chef has an array A consisting of N integers. He also has an intger K.

Chef wants you to find out number of different arrays he can obtain from array A by applying the following operation exactly K times.

Pick some element in the array and multiply it by -1

As answer could be quite large, print it modulo 10^{9} + 7.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space separated integers N, K as defined above.
The second line contains N space-separated integers A_{1}, A_{2}, ..., A_{N} denoting the elements of the array.

------ Output ------ 

For each test case, output a single line containing an integer corresponding to the number of different arrays Chef can get modulo 10^{9} + 7.

------ Constraints ------ 

$1 ≤ T ≤ 10$
$1 ≤ N, K ≤ 10^{5}$
$-10^{6} ≤ A_{i} ≤ 10^{6}$

------ Subtasks ------ 

$Subtask #1 (10 points) : N, K ≤ 10$
$Subtask #2 (30 points) : N, K ≤ 100$
$Subtask #3 (60 points) : N, K ≤ 10^{5}$

----- Sample Input 1 ------ 
3

1 3

100

3 1

1 2 1

3 2

1 2 1
----- Sample Output 1 ------ 
1

3

4
----- explanation 1 ------ 
Example case 1.
Chef has only one element and must apply the operation 3 times to it. After applying the operations, he will end up with -100. That is the only array he will get.

Example case 2.
Chef can apply operation to one of three elements. So, he can obtain three different arrays.

Example case 3.
Note that other than applying operation to positions (1, 2), (1, 3), (2, 3), Chef can also apply the operation twice on some element and get the original.

In summary, Chef can get following four arrays.

[1, 2, 1]
[-1, -2, 1]
[-1, 2, -1]
[1, -2, -1]
"""

MOD = 10**9 + 7
p = 10**6 + 5
fact = [0] * p
fact[0] = 1
for i in range(1, p):
    fact[i] = fact[i - 1] * i % MOD

def MI(a, MOD):
    return pow(a, MOD - 2, MOD)

def nck(n, k):
    if n == k or k == 0:
        return 1
    if n < k:
        return 0
    return fact[n] * MI(fact[k], MOD) % MOD * MI(fact[n - k], MOD) % MOD % MOD

def count_different_arrays(n, k, array):
    f = 0
    if 0 in array:
        f = 1
    n = n - array.count(0)
    ans = 0
    for x in range(0, min(n + 1, k + 1)):
        if (k - x) % 2 == 0 or f:
            ans = (ans + nck(n, x)) % MOD
    return ans