"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

Masha has $N$ minions. Each minion has two characteristics: power $a$ and endurance $b$. Masha thinks that a non-empty set of minions $\{m_{1}, m_{2}, \dots, m_{k}\}$ with characteristics $(a_{m_{1}},b_{m_{1}}), (a_{m_{2}},b_{m_{2}}), \dots, (a_{m_{k}},b_{m_{k}})$ is *good* if the mean endurance of this set doesn't exceed the minimum power in it, i.e. if $min(a_{m_{1}}, a_{m_{2}}, \dots, a_{m_{k}}) ≥ (b_{m_{1}}+b_{m_{2}}+\dots+b_{m_{k}}) / k$.

Masha would like to choose a good subset of her minions and give these minions to Mark. Your task is to calculate the maximum number of minions Masha can give to Mark.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The following $N$ lines describe minions. Each of these lines contains two space-separated integers $a$ and $b$ denoting the power and endurance of one minion.

------  Output ------
For each test case, print a single line containing one number — the size of the largest good set of minions, or $0$ if no such set exists.

------  Constraints  ------
$1 ≤ T ≤ 1,000$
$1 ≤ N ≤ 4\cdot10^{5}$
$1 ≤ a, b ≤ 10^{9}$
the sum of $N$ for all test cases does not exceed $4\cdot10^{5}$

----- Sample Input 1 ------ 
2
3
1 4
3 3
2 1
2
3 5
1 4
----- Sample Output 1 ------ 
2
0
----- explanation 1 ------ 
Example case 1: The set of minions $\{2, 3\}$ is good, since $\mathrm{min}(3,2) ≥ (3+1)/2$.

Example case 2: There is no non-empty good subset of minions.
"""

def max_good_subset_size(test_cases):
    results = []
    
    for minions in test_cases:
        N = len(minions)
        if N == 0:
            results.append(0)
            continue
        
        mas_p = [(a, b, i) for i, (a, b) in enumerate(minions)]
        mas_e = mas_p[:]
        
        mas_e.sort(key=lambda el: el[1])
        mas_p.sort(key=lambda el: (el[0], -el[1]))
        
        ans = 0
        b = -1
        e = 0
        processed_p = set()
        processed_num = 0
        
        for cur_p_i in range(N):
            p = mas_p[cur_p_i][0]
            while b < N - 1:
                if mas_e[b + 1][2] in processed_p:
                    b += 1
                    processed_num += 1
                    continue
                if p * (b + 1 + 1 - processed_num) >= e + mas_e[b + 1][1]:
                    b += 1
                    e += mas_e[b][1]
                    processed_p.add(mas_e[b][2])
                    continue
                else:
                    break
            if mas_p[cur_p_i][2] in processed_p:
                ans = max(ans, b + 1 - processed_num)
                e -= mas_p[cur_p_i][1]
                processed_num += 1
            else:
                processed_p.add(mas_p[cur_p_i][2])
        
        results.append(ans)
    
    return results