"""
QUESTION:
The fight between Sardar Khan and Sultan to control Wasseypur is getting very intensifying. Sultan has asked Ramadhir to supply him with automatic guns in an attempt to dominate the battlefield. The Sardar family must also buy automatic guns or risk annihilation.

The gun merchant Sardar is buying guns from has N guns in stock, the i-th of which has type A_{i}. He sells these guns according to the following peculiar rules:
Only one person can buy guns at a time.
For all 1 < i ≤ N, he will sell the i-th gun only if the (i-1)-th gun has already been sold to somebody. The first gun can be sold directly with no restriction.
Once some guns are sold to a person and they leave, they will not be allowed to come back in later and purchase any more guns.

As a result, any buyer can only own a consecutive set of guns - if the first unsold gun when they enter has index L, they can only buy guns L, L+1, L+2, \dots, R where L ≤ R ≤ N, and the choice of R is left to them.

Sardar Khan wants his lackeys to visit the gun merchant and buy all the guns. The *intimidation power* of a lackey is the number of distinct types of guns in his possession. The total intimidation power Sardar Khan gets from his lackeys is the product of all of their individual intimidation powers (to ensure this value is non-zero, only consider the product over all lackeys who purchase at least one weapon from this merchant).
Sardar can send as few or as many lackeys to the merchant as he likes, as long as every weapon is purchased by at least one of them.

Sardar obviously would like to maximize his intimidation power. Find out what this maximum value is, given that his lackeys buy guns optimally. The answer can be large, so print it modulo 10^{9} + 7.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T lines follows.
- The first line of each test case contains a single integer N, the number of guns the merchant has for sale.
- The second line of each test case contains N space-separated integers, A_{1},A_{2},\ldots,A_{N}; where A_{i} is the type of the i-th gun.

------ Output Format ------ 

For each test case, output a single line containing one integer - the maximum intimidation power Sardhar can achieve, modulo 10^{9}+7.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$2 ≤ N ≤ 2\cdot 10^{5}$
$0 ≤ A_{i} ≤ 10^{9}$
- Sum of $N$ over all test cases is less than or equal to $2\cdot 10^{5}$

----- Sample Input 1 ------ 
2
7
1 1 1 2 3 4 9
10
1 2 3 3 3 4 4 5 6 9
----- Sample Output 1 ------ 
6
24

----- explanation 1 ------ 
Test Case 1

The first lackey buys the guns $(1, 1)$. The second lackey buys $(1, 2)$ and the third lackey buys $(3, 4, 9)$. The number of unique guns the lackeys now have are $1, 2, 3$ respectively.

The total intimidation power Sardar Khan gets is $ 1 \cdot  2 \cdot 3 = 6 $. 

Another possible distribution achieving the same value is $(1, 1, 1, 2)$ and $(3, 4, 9)$ which requires only $2$ lackeys.

It can be verified that there is no way to achieve a higher value.

Test Case 2

The first lackey buys the guns $(1, 2, 3)$. The second lackey buys $(3, 3, 4)$ and the third lackey buys $(4, 5, 6, 9)$. The number of unique guns the lackeys now have are $3, 2, 4$ respectively.

The total intimidation power Sardar Khan gets is $ 3 \cdot 2 \cdot 4 = 24 $.
"""

from math import log

MOD = 10 ** 9 + 7

def int23compare(lst):
    (count2, count3) = lst
    return count2 * log(2) + count3 * log(3)

def calculate_max_intimidation_power(test_cases):
    results = []
    
    for (n, a) in test_cases:
        if n <= 3:
            result = len(set(a))
        else:
            prev3 = a[0]
            prev3_count = [0, 0]
            prev2 = a[1]
            if len(set(a[:2])) == 1:
                prev2_count = [0, 0]
            else:
                prev2_count = [1, 0]
            prev1 = a[2]
            if len(set(a[:3])) == 1:
                prev1_count = [0, 0]
            elif len(set(a[:3])) == 2:
                prev1_count = [1, 0]
            else:
                prev1_count = [0, 1]
            for i in range(3, n):
                curr = a[i]
                x3 = prev3_count[:]
                num3 = len({prev2, prev1, curr})
                if num3 == 2:
                    x3[0] += 1
                elif num3 == 3:
                    x3[1] += 1
                x2 = prev2_count[:]
                num2 = len({prev1, curr})
                if num2 == 2:
                    x2[0] += 1
                x1 = prev1_count[:]
                max_value = max(x3, x2, x1, key=int23compare)
                prev3_count = prev2_count[:]
                prev2_count = prev1_count[:]
                prev1_count = max_value[:]
                prev3 = prev2
                prev2 = prev1
                prev1 = curr
            result = pow(2, max_value[0], MOD) * pow(3, max_value[1], MOD)
        result %= MOD
        results.append(result)
    
    return results