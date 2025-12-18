"""
QUESTION:
Read problems statements in Russian also. 
Chef likes shopping, and especially he likes to buy oranges. But right now he is short of money. He has only k rubles. There are n oranges. The i-th one costs cost_{i} rubles and has weight equal to weight_{i}. Chef wants to buy a set of oranges with the maximal possible weight. Please help him, and tell him this weight.

------ Input ------ 

The first line of the input contains an integer T  denoting the number of test cases. The first line of each test case contains two numbers n and k. The following n lines contain two numbers cost_{i} and weight_{i} respectively. 

------ Output ------ 

For each test case, output a single line containing maximal weight among all the affordable sets of oranges. 

------ Constraints ------ 

$1 ≤ T ≤  250 $
$1 ≤ n ≤  10 $
$1 ≤ k ≤  100000000 $
$1 ≤ weight_{i} ≤  100000000 $
$1 ≤ cost_{i} ≤  100000000 $

------ Scoring ------ 

Subtask 1 (30 points): All the oranges' weights equals to 1.

Subtask 2 (30 points):   N = 5  

Subtask 2 (40 points):  See the constraints 

----- Sample Input 1 ------ 
2
1 3
2 2
3 4
2 1
2 2
3 5
----- Sample Output 1 ------ 
2
5
"""

from itertools import combinations

def max_affordable_weight(test_cases):
    results = []
    
    for case in test_cases:
        n, k, oranges = case
        a = [orange[0] for orange in oranges]
        b = [orange[1] for orange in oranges]
        c = list(range(n))
        
        ans = 0
        for r in range(1, n + 1):
            x = combinations(c, r)
            for i in x:
                cost = 0
                weight = 0
                for j in i:
                    cost += a[j]
                    weight += b[j]
                if cost <= k and weight > ans:
                    ans = weight
        
        results.append(ans)
    
    return results