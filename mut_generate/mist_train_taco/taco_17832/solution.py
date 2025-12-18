"""
QUESTION:
The customer telephone support center of the computer sales company called JAG is now in- credibly confused. There are too many customers who request the support, and they call the support center all the time. So, the company wants to figure out how many operators needed to handle this situation.

For simplicity, let us focus on the following simple simulation.

Let N be a number of customers. The i-th customer has id i, and is described by three numbers, Mi, Li and Ki. Mi is the time required for phone support, Li is the maximum stand by time until an operator answers the call, and Ki is the interval time from hanging up to calling back. Let us put these in other words: It takes Mi unit times for an operator to support i-th customer. If the i-th customer is not answered by operators for Li unit times, he hangs up the call. Ki unit times after hanging up, he calls back.

One operator can support only one customer simultaneously. When an operator finish a call, he can immediately answer another call. If there are more than one customer waiting, an operator will choose the customer with the smallest id.

At the beginning of the simulation, all customers call the support center at the same time. The simulation succeeds if operators can finish answering all customers within T unit times.

Your mission is to calculate the minimum number of operators needed to end this simulation successfully.



Input

The input contains multiple datasets. Each dataset has the following format:

N T
M1 L1 K1
.
.
.
MN LN KN


The first line of a dataset contains two positive integers, N and T (1 ≤ N ≤ 1000, 1 ≤ T ≤ 1000). N indicates the number of customers in the dataset, and T indicates the time limit of the simulation.

The following N lines describe the information of customers. The i-th line contains three integers, Mi, Li and Ki (1 ≤ Mi ≤ T , 1 ≤ Li ≤ 1000, 1 ≤ Ki ≤ 1000), describing i-th customer's information. Mi indicates the time required for phone support, Li indicates the maximum stand by time until an operator answers the call, and Ki indicates the is the interval time from hanging up to calling back.

The end of input is indicated by a line containing two zeros. This line is not part of any dataset and hence should not be processed.

Output

For each dataset, print the minimum number of operators needed to end the simulation successfully in a line.

Example

Input

3 300
100 50 150
100 50 150
100 50 150
3 300
100 50 150
100 50 150
200 50 150
9 18
3 1 1
3 1 1
3 1 1
4 100 1
5 100 1
5 100 1
10 5 3
10 5 3
1 7 1000
10 18
1 2 3
2 3 4
3 4 5
4 5 6
5 6 7
6 7 8
7 8 9
8 9 10
9 10 11
10 11 12
0 0


Output

2
3
3
4
"""

def minimum_operators_needed(N, T, customers):
    def check(N, C, T, x):
        used = [0] * N
        S = [0] * (T + 1)
        cap = x
        f = 0
        for t in range(T):
            cap += S[t]
            if cap == 0:
                continue
            for i in range(f, N):
                if used[i]:
                    continue
                (m, l, k) = C[i]
                if t + m > T:
                    break
                if t % (l + k) <= l:
                    used[i] = 1
                    S[t + m] += 1
                    cap -= 1
                    if i == f:
                        while f < N and used[f]:
                            f += 1
                    if cap == 0:
                        break
        cap += S[T]
        return sum(used) == N and cap == x

    for x in range(N + 1):
        if check(N, customers, T, x):
            return x
    return -1  # In case no solution is found, though the problem guarantees a solution