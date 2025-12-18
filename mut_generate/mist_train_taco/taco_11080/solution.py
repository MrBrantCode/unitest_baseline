"""
QUESTION:
You have a knapsack with the capacity of $W$. There are also $n$ items, the $i$-th one has weight $w_i$.

You want to put some of these items into the knapsack in such a way that their total weight $C$ is at least half of its size, but (obviously) does not exceed it. Formally, $C$ should satisfy: $\lceil \frac{W}{2}\rceil \le C \le W$.

Output the list of items you will put into the knapsack or determine that fulfilling the conditions is impossible.

If there are several possible lists of items satisfying the conditions, you can output any. Note that you don't have to maximize the sum of weights of items in the knapsack.


-----Input-----

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 10^4$). Description of the test cases follows.

The first line of each test case contains integers $n$ and $W$ ($1 \le n \le 200000$, $1\le W \le 10^{18}$).

The second line of each test case contains $n$ integers $w_1, w_2, \dots, w_n$ ($1 \le w_i \le 10^9$) — weights of the items.

The sum of $n$ over all test cases does not exceed $200000$.


-----Output-----

For each test case, if there is no solution, print a single integer $-1$.

If there exists a solution consisting of $m$ items, print $m$ in the first line of the output and $m$ integers $j_1$, $j_2$, ..., $j_m$ ($1 \le j_i \le n$, all $j_i$ are distinct) in the second line of the output  — indices of the items you would like to pack into the knapsack.

If there are several possible lists of items satisfying the conditions, you can output any. Note that you don't have to maximize the sum of weights items in the knapsack.


-----Examples-----

Input
3
1 3
3
6 2
19 8 19 69 9 4
7 12
1 1 1 17 1 1 1
Output
1
1
-1
6
1 2 3 5 6 7


-----Note-----

In the first test case, you can take the item of weight $3$ and fill the knapsack just right.

In the second test case, all the items are larger than the knapsack's capacity. Therefore, the answer is $-1$.

In the third test case, you fill the knapsack exactly in half.
"""

import math

def find_knapsack_items(n, W, weights):
    l = [[weights[i], i + 1] for i in range(n)]
    l.sort()
    
    total_weight = 0
    start = 0
    end = n - 1
    inf = -1
    ans = -1
    
    for i in range(n):
        if l[i][0] >= math.ceil(W / 2) and l[i][0] <= W:
            inf = i
            ans = 1
            start = i
            end = i
            break
        elif l[i][0] < math.ceil(W / 2):
            total_weight += l[i][0]
            if total_weight >= math.ceil(W / 2):
                end = i
                ans = 1
                break
    
    if ans != -1:
        selected_items = [l[i][1] for i in range(start, end + 1)]
        return len(selected_items), selected_items
    else:
        return None