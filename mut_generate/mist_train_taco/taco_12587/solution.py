"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

Alice and Bob, both have to drink water. But they both don't want to go, so they will play a game to decide who will fetch water for both of them. Alice will choose a number randomly between 1 and N (both inclusive) and Bob will choose a number randomly between 1 and M (both inclusive). Both will write their numbers on a slip of paper. If sum of numbers choosen by both is odd, then Alice will go, else Bob will go.

What is probability that Alice will go?

------ Input ------ 

First line contains, T, the number of testcases. Each testcase consists of N and M in one line, separated by a space.

------ Output ------ 

For each test case, output a single line containing probability as an irreducible fraction.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N,M ≤ 10^{9}$

----- Sample Input 1 ------ 
3
1 1
1 2
2 3
----- Sample Output 1 ------ 
0/1
1/2
1/2
----- explanation 1 ------ 
#test1: The only way is when Alice and Bob both choose 1. So, Alice won't have to go because sum is even.
#test2: The different ways are (1,1) and (1,2), where first term denotes the number choosen by Alice. So of all possible cases (ie. 2) in only 1 case Alice has to go. Therefore, probability is 1/2.
#test3: The different ways are (1,1), (1,2), (1,3), (2,1), (2,2), (2,3) where first term denotes the number choosen by Alice. So of all possible cases (ie. 6) in only 3 cases Alice has to go. Therefore, probability is 1/2.
"""

from fractions import Fraction

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def calculate_alice_going_probability(N, M):
    total_pairs = N * M
    odd_sum_pairs = total_pairs // 2
    
    # Calculate the greatest common divisor (GCD) to simplify the fraction
    common_divisor = gcd(odd_sum_pairs, total_pairs)
    
    # Simplify the fraction
    probability = Fraction(odd_sum_pairs // common_divisor, total_pairs // common_divisor)
    
    return probability