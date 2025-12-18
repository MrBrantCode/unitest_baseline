"""
QUESTION:
A and B are brothers and like playing with marbles.Their mother buys them N marbles to play with.The preciousness of each marble is a natural number from 1 to N and no two marbles have same preciousness.
Since A and B are good at maths they want to divide all those N marbles among them in such a way that sum of the preciousness of all marbles that A receives and sum of the preciousness of all marbles that B receives after distribution are co-primes i.e the gcd(greatest common divisor) of their sum is 1.
Also the absolute value of difference between the sum of the preciousness of marbles of A and B should be exactly M.
Help A and B in finding whether such a distribution of N marbles between them is possible or not.

Formally, you have to tell whether you can distribute first N natural numbers in two sets such that the absolute difference of the sum of numbers in the two sets is equal to M and the gcd of their sum is 1.

Note that one of the set can be empty and greatest common divisor of 0 and k is k

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two integers N  and M denoting the number of marbles and the absolute difference of sum respectively. 
 
------ Output ------ 

For each test case, output a single line.

Print “Yes” if there exist a valid distribution of marbles between A and B else print “No”.

------ Constraints ------ 

$1 ≤ T ≤ 20$
$1 ≤ N ≤ 1,000,000,000$

$0 ≤ M ≤ 10^{18}$

----- Sample Input 1 ------ 
2
5 7
1 2
----- Sample Output 1 ------ 
Yes
No
"""

from math import gcd

def can_distribute_marbles(N, M):
    # Calculate the sum of the first N natural numbers
    sum1 = N * (N + 1) // 2
    
    # Check if the sum1 + M is even, which is necessary for the distribution
    if (sum1 + M) % 2 != 0:
        return "No"
    
    # Calculate the two sums a and b
    a = (sum1 + M) // 2
    b = sum1 - a
    
    # Check if the absolute difference is exactly M
    if abs(a - b) != M:
        return "No"
    
    # Check if the gcd of a and b is 1
    if gcd(a, b) == 1:
        return "Yes"
    else:
        return "No"