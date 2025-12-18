"""
QUESTION:
Consider the infinite x$x$ axis. There are N$N$ impacts on this X-axis at integral points (X1$X_1$,X2$X_2$,....XN$X_N$)  (all distinct) . An impact at a point X$X$i propagates such that at a point X$X$0, the effect of the impact is K|Xi−X0|$K^{|X_i - X_0|}$. Given the point X0$X_0$, N$N$ and K$K$. Assume the total impact on X0$X_0$ is M$M$, find if it is possible to do so.Note: You are not required to find the set X

Formally print "yes" if this is possible and "no" if not possible.

-----Input:-----
- First line will contain T$T$, number of testcases. Then the testcases follow. 
-  Each testcase contains of a single line of input, four integers N$N$,K$K$,M$M$,X$X$0 

-----Output:-----
-  The output of each test case is either "yes" or "no"

-----Constraints -----
-  1≤T≤1000$1\leq T \leq 1000$
-  1≤N≤100$1\leq N \leq 100$
-  1≤K≤1000$1\leq K \leq 1000$
-  1≤M≤1018$1\leq M \leq 10^{18}$
-  −109≤X0≤109$-10^9 \leq X_0 \leq 10^9$ 

-----Sample Input:-----
	2

4 3 10 10

2 3 10 10

-----Sample Output:-----
	no

yes
"""

def is_impact_possible(N, K, M, X0):
    if K == 1:
        if N == M:
            return 'yes'
        else:
            return 'no'
    elif M % K > 1:
        return 'no'
    elif K == 2:
        stack = []
        var = 0
        while M != 0:
            var += M % K
            stack.append(M % K)
            M //= K
        if var > N:
            return 'no'
        elif var == N:
            return 'yes'
        else:
            for p in range(100):
                for q in range(2, len(stack)):
                    if stack[q - 1] == 0 and stack[q] >= 1:
                        stack[q - 1] = 2
                        stack[q] -= 1
                        var += 1
                        if var == N:
                            return 'yes'
            if var < N:
                return 'no'
    else:
        temp = 0
        rog = 1
        while M != 0:
            if M % K > 2:
                rog = 0
                return 'no'
            temp += M % K
            M //= K
        if rog:
            if temp == N:
                return 'yes'
            else:
                return 'no'