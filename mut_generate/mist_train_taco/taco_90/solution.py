"""
QUESTION:
You are given a sequence A, where its elements are either in the form + x or -, where x is an integer.

For such a sequence S where its elements are either in the form + x or -, define f(S) as follows:

  * iterate through S's elements from the first one to the last one, and maintain a multiset T as you iterate through it. 
  * for each element, if it's in the form + x, add x to T; otherwise, erase the smallest element from T (if T is empty, do nothing). 
  * after iterating through all S's elements, compute the sum of all elements in T. f(S) is defined as the sum. 



The sequence b is a subsequence of the sequence a if b can be derived from a by removing zero or more elements without changing the order of the remaining elements. For all A's subsequences B, compute the sum of f(B), modulo 998 244 353.

Input

The first line contains an integer n (1≤ n≤ 500) — the length of A.

Each of the next n lines begins with an operator + or -. If the operator is +, then it's followed by an integer x (1≤ x<998 244 353). The i-th line of those n lines describes the i-th element in A.

Output

Print one integer, which is the answer to the problem, modulo 998 244 353.

Examples

Input


4
-
+ 1
+ 2
-


Output


16

Input


15
+ 2432543
-
+ 4567886
+ 65638788
-
+ 578943
-
-
+ 62356680
-
+ 711111
-
+ 998244352
-
-


Output


750759115

Note

In the first example, the following are all possible pairs of B and f(B):

  * B= {}, f(B)=0. 
  * B= {-}, f(B)=0. 
  * B= {+ 1, -}, f(B)=0. 
  * B= {-, + 1, -}, f(B)=0. 
  * B= {+ 2, -}, f(B)=0. 
  * B= {-, + 2, -}, f(B)=0. 
  * B= {-}, f(B)=0. 
  * B= {-, -}, f(B)=0. 
  * B= {+ 1, + 2}, f(B)=3. 
  * B= {+ 1, + 2, -}, f(B)=2. 
  * B= {-, + 1, + 2}, f(B)=3. 
  * B= {-, + 1, + 2, -}, f(B)=2. 
  * B= {-, + 1}, f(B)=1. 
  * B= {+ 1}, f(B)=1. 
  * B= {-, + 2}, f(B)=2. 
  * B= {+ 2}, f(B)=2. 



The sum of these values is 16.
"""

MOD = 998244353

def calculate_subsequence_sum(n, sequence):
    ans = 0
    arr = []
    for i in range(n):
        a = sequence[i].split()
        if len(a) == 2:
            arr.append(int(a[1]))
        else:
            arr.append(0)
    
    for cur in range(n):
        if arr[cur]:
            dp = [0] * (n + 1)
            dp[0] = 1
            for (j, a) in enumerate(arr):
                if j == cur:
                    dp = [0] + dp[:n]
                elif a == 0:
                    dp[0] = (2 * dp[0] + dp[1]) % MOD
                    for i in range(1, n):
                        dp[i] = (dp[i] + dp[i + 1]) % MOD
                elif a < arr[cur] or (a == arr[cur] and j < cur):
                    if j < cur:
                        for i in range(n, 0, -1):
                            dp[i] = (dp[i - 1] + dp[i]) % MOD
                    else:
                        for i in range(n, 1, -1):
                            dp[i] = (dp[i - 1] + dp[i]) % MOD
                        dp[0] = dp[0] * 2 % MOD
                else:
                    dp = [d * 2 % MOD for d in dp]
            ans = (ans + (sum(dp) - dp[0]) * arr[cur]) % MOD
    
    return ans