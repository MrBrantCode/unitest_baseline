"""
QUESTION:
Coach Chef has selected all the players and now he has to separate them into 2 teams, $A$ and $B$.

Each player must be included in exactly one of the 2 teams and each player $x$, has a skill level $S_{x}$. It is not necessary for both teams to have equal number of players, but they have to be non-empty.

Since the number of players is way too high, Chef doesn't have an actual list of every player individually. Instead, he keeps a list of $N$ pairs $ {X_{i}, Y_{i} }$, which tells him that there are $Y_{i}$ players with skill level $X_{i}$.

Chef thinks that a division into 2 teams is Good, if the skill value of every player in A divides the skill value of every player in B. More formally, $S_{b} \bmod S_{a} = 0$, ∀ a ∈ A, b ∈ B.

Since he is busy, can you help him find total number of Good divisions? Since the answer can be very large, print it modulo $998244353$.

NOTE : 2 divisions are considered different if there exists any player $x$ belonging to different teams in the 2 divisions. (See example for more clarity). 

------  Input  ------ 

The first line of the input contains a single integer $T$ denoting the number of test cases. The description of
$T$ test cases follows.
The first line for each testcase has a single integer $N$, denoting the number of pairs in Chef's list. 
$N$ lines follow. Each contains 2 space separated integers $X_{i}$ and $Y_{i}$, denoting Chef has $Y_{i}$ players with skill level $X_{i}$.

------  Output  ------ 

Output one integer for every testcase. The number of total Good divisions, modulo $998244353$.

------ Constraints ------ 

$ $1 ≤ T, N ≤ 10^{5}$
$$ $1 ≤ X_{i} ≤ 10^{9}, X_{i} \neq X_{j}$ for $i \neq j$
$$ $1 ≤ Y_{i} ≤ 10^{5}$
$$ Sum of $N$ over all testcases does not exceed $10^{5}$

------ Example Input ------ 

5

1

10 1

3

1 1

3 1

6 1

3

1 1

3 2

6 1

10

1 30

2 40

3 30

6 50

12 100

18 500

216 400

24 999

432 9999

864 123

1

10 1000

------ Example Output ------ 

0

2

4

128248098

23226275

------ Explanation ------ 

Example Case 1: Only one player P1. No way to split into teams.

Example Case 2: 3 players total, P1, P2 & P3 with skill level 1, 3 & 6 respectively. Possible divisions:

$ A=[P1], B=[P2, P3]
$$ A=[P1, P2], B=[P3]Example Case 3: 4 players total, P1, P2, P3 & P4 with skill levels 1, 3, 3 & 6 respectively. Possible divisions :
 
$ A=[P1], B=[P2, P3, P4]
$$ A=[P1, P2], B=[P3, P4]
$$ A=[P1, P3], B=[P2, P4]
$$ A=[P1, P2, P3], B=[P4]
"""

def count_good_divisions(test_cases):
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    
    mod = 998244353
    results = []
    
    for a in test_cases:
        n = len(a)
        a.sort()
        
        if n == 1:
            results.append((pow(2, a[0][1], mod) - 2) % mod)
            continue
        
        prefixlcm = []
        lcm = 1
        for i in range(n):
            lcm = lcm * a[i][0] // gcd(lcm, a[i][0])
            prefixlcm.append(lcm)
        
        suffixgcd = [0] * n
        g = 0
        for i in range(n - 1, -1, -1):
            g = gcd(g, a[i][0])
            suffixgcd[i] = g
        
        res = 0
        b = 0
        for i in range(n - 1):
            if prefixlcm[i] > 1000000000.0:
                b = 1
                break
            if suffixgcd[i] % prefixlcm[i] == 0:
                res = (res + pow(2, a[i][1], mod) - 2) % mod
            if i + 1 < n and suffixgcd[i + 1] % prefixlcm[i] == 0:
                res = (res + 1) % mod
        
        if not b and suffixgcd[n - 1] % prefixlcm[n - 1] == 0:
            res = (res + pow(2, a[n - 1][1], mod) - 2) % mod
        
        results.append(res)
    
    return results