"""
QUESTION:
Not everything in Wasseypur is about gangs and guns. There are normal people too! Ashok is a simple farmer who has the misfortune of living in Wasseypur. He plants his seeds and works the land with his family like an honest man.  

Through his hard work and grit he can turn his seeds into lush crops. However, not all seeds are equal - some seeds are good, some are bad. Seeds can be one of 4 types - \{-2, -1, 1, 2\}. Ashok goes to the farmer's market to buy some seeds where he meets Uday, an eccentric rich merchant. Ashok doesn't have enough money to buy all the seeds he can plant. Taking pity on him, Uday proposes a strange game.

Uday sets out N seeds out in a pattern resembling a tree. Ashok can then choose one simple path in this tree and take every seed along this path. The path must not be empty, i.e, it should contain at least one vertex of the tree.

The total yield of the seeds Ashok receives equals the product of all their types. Given this tree and the type of seed placed at each vertex, what is the maximum yield Ashok can obtain?

The answer can be large, so print it modulo 10^{9} + 7.
If the answer is negative, print the *positive* remainder obtained on division by 10^{9} + 7 - that is, if the answer is -1, print 1000000006.

------ Input Format ------ 

- The first line of input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N, denoting the number of seeds.
- Each of the next N - 1 lines contains two integers a and b, denoting that the a-th and b-th seeds are connected in tree.
- The (N+1)-th line of each test case consists of N integers, S_{1}, S_{2}, S_{3},\ldots S_{N}, S_{i} represents the type of the i_{th} seed.

------ Output Format ------ 

For each test case, print a single integer denoting the maximum yield that Ashok can get modulo 10^{9} +7.

------ Constraints ------ 

$1 ≤ T ≤ 10000$
$1 ≤ N ≤ 10^{5}$
$S_{i} \in \{-2, -1, 1, 2\}$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
2
5
1 2
2 3
3 4
1 5
2 2 -1 -2 2
5
1 2
1 3
1 4
1 5
-1 -1 -1 -1 2
----- Sample Output 1 ------ 
16
2

----- explanation 1 ------ 
Test case 1:

One possible path giving the maximum product is $\{ 5, 1, 2, 3, 4 \}$.

Test case 2:

One possible path giving maximum product is $\{ 2, 1, 5 \}$.
"""

import sys
from collections import defaultdict

def calculate_maximum_yield(T, test_cases):
    M = 10 ** 9 + 7
    results = []
    
    for case in test_cases:
        N, edges, seeds = case
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        ans = []
        
        def helper(node, prev):
            min_vals = []
            max_vals = []
            curr = seeds[node - 1]
            for ele in graph[node]:
                if ele != prev:
                    a, b = helper(ele, node)
                    min_vals.append((a, ele))
                    max_vals.append((b, ele))
            if not len(min_vals):
                ans.append(curr)
                return (min(1, curr), max(1, curr))
            min_vals.sort()
            max_vals.sort(reverse=True)
            temp = [1]
            temp.append(curr * min_vals[0][0])
            temp.append(curr * max_vals[0][0])
            if len(min_vals) == 1:
                u = min_vals[0][0]
                ans.append(u * curr)
                u = max_vals[0][0]
                ans.append(u * curr)
            else:
                u1, v1 = min_vals[0][0], min_vals[1][0]
                ans.append(u1 * v1 * curr)
                u2, v2 = max_vals[0][0], max_vals[1][0]
                ans.append(u2 * v2 * curr)
                if min_vals[0][1] == max_vals[0][1]:
                    ans.append(u1 * v2 * curr)
                    ans.append(u2 * v1 * curr)
                else:
                    ans.append(u1 * u2 * curr)
            return (min(temp), max(temp))
        
        helper(1, N + 1)
        results.append(max(ans) % M)
    
    return results