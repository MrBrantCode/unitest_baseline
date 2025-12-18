"""
QUESTION:
Mr Nikhil has k Children. They are suffering from a disease called Gasomia . 
According to his family Doctor , Child 1 requires atleast x1 tablets , Child 2 requires atleast  x2 ......... Child k requires atleast xk tablets.
As Nikhil got job in Golden Ship,he bought m tablets and wants to distribute all the tablets among his children.Can you tell him the number of ways of distributing tablets among children in such a way,that all the children get satisfied.
As the numbers of ways can be very large, print ans mod 1000000007

Input
First line of the input contains T , denoting number of test cases

For each test case it  contains two integers k and m denoting— number of children and the number of tablets he have respectively.

Then follow k  numbers , denoting minimum tablets needed by child i, 1≤ i ≤ k

Output
Print the number of ways % 1000000007.

SAMPLE INPUT
1
2 3
1 1

SAMPLE OUTPUT
2

Explanation

In the Sample Test Case ,Nikhil has 2 children x1 and x2 and he bought 3 tablets.
x1 needs atleast 1 tablet
x2 needs atleast 1 tablet
so he can distribute in 2 ways i.e (1,2) and (2,1)
"""

def count_ways_to_distribute_tablets(k, m, requirements, mod=1000000007):
    # Precompute factorials up to the maximum possible value
    max_fact = 100000
    fact = [1] * (max_fact + 1)
    for x in range(2, max_fact + 1):
        fact[x] = (fact[x - 1] * x) % mod
    
    # Calculate the total number of tablets required
    total_required = sum(requirements)
    
    # Calculate the number of extra tablets available
    n = m - total_required
    
    # If the number of extra tablets is negative, return 0
    if n < 0:
        return 0
    
    # Calculate the number of ways to distribute the tablets
    # Using the combination formula C(n + k - 1, k - 1)
    numerator = fact[n + k - 1]
    denominator = (fact[k - 1] * fact[n]) % mod
    inverse_denominator = pow(denominator, mod - 2, mod)
    
    return (numerator * inverse_denominator) % mod