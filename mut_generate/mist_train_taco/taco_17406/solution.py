"""
QUESTION:
Chef is operating a slush machine. The machine produces slush drinks with $M$ flavors (numbered $1$ through $M$); for each valid $i$, the maximum number of drinks with flavour $i$ the machine can produce is $C_i$.
Chef expects $N$ customers to come buy slush drinks today. The customers are numbered $1$ through $N$ in the order in which they buy the drinks. For each valid $i$, the favorite flavour of the $i$-th customer is $D_i$ and this customer is willing to pay $F_i$ units of money for a drink with this flavour, or $B_i$ units of money for a drink with any other flavuor. Whenever a customer wants to buy a drink:
- if it is possible to sell this customer a drink with their favourite flavour, Chef must sell them a drink with this flavour
- otherwise, Chef must sell this customer a drink, but he may choose its flavour
Chef wants to make the maximum possible profit. He is asking you to help him decide the flavours of the drinks he should sell to the customers in order to maximise the profit.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $M$ space-separated integers $C_1, C_2, \ldots, C_M$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains three space-separated integers $D_i$, $F_i$ and $B_i$.

-----Output-----
For each test case, print two lines:
- The first of these lines should contain a single integer — the maximum profit.
- The second line should contain $N$ space-separated integers denoting the flavours of the drinks Chef should sell, in this order.
If there are multiple solutions, you may find any one.

-----Constraints-----
- $1 \le T \le 1,000$
- $2 \le N, M \le 10^5$
- $1 \le D_i \le M$ for each valid $i$
- $1 \le C_i \le N$ for each valid $i$
- $1 \le B_i < F_i \le 10^9$ for each valid $i$
- $C_1+C_2+\ldots+C_M \ge N$
- the sum of $N$ over all test cases does not exceed $10^6$
- the sum of $M$ over all test cases does not exceed $10^6$

-----Example Input-----
1
5 3
1 2 3
2 6 3
2 10 7
2 50 3
1 10 5
1 7 4

-----Example Output-----
33
2 2 3 1 3
"""

def maximize_profit(T, test_cases):
    results = []
    
    for test_case in test_cases:
        N, M, C, customers = test_case
        s = sum(C)
        s1 = 0
        ans = []
        q = []
        q1 = []
        
        if s >= N:
            p = C[:]
            for i in range(N):
                d, f, b = customers[i]
                if p[d - 1] > 0:
                    s1 += f
                    p[d - 1] -= 1
                    ans.append(d)
                else:
                    s1 += b
                    ans.append(0)
                    q.append(i)
            
            for i in range(M):
                if p[i] != 0:
                    q1.append([i, p[i]])
            
            x = 0
            for i in q:
                if q1[x][1] != 0:
                    ans[i] = q1[x][0] + 1
                    q1[x][1] -= 1
                else:
                    x += 1
                    ans[i] = q1[x][0] + 1
                    q1[x][1] -= 1
        
        results.append((s1, ans))
    
    return results