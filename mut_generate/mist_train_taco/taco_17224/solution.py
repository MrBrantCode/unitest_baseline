"""
QUESTION:
Chef has 3 numbers A, B and C. 

Chef wonders if it is possible to choose *exactly* two numbers out of the three numbers such that their sum is odd.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of three integers A, B, C.

------ Output Format ------ 

For each test case, output YES if you can choose exactly two numbers with odd sum, NO otherwise.

The output is case-insensitive. Thus, the strings YES, yes, yeS, and Yes are all considered the same.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ A, B, C ≤ 10$

----- Sample Input 1 ------ 
4
1 2 3
8 4 6
3 3 9
7 8 6

----- Sample Output 1 ------ 
YES
NO
NO
YES

----- explanation 1 ------ 
Test case 1: Chef can choose $2$ and $3$ since $2 + 3 = 5$ and $5$ is odd.

Test case 2: It can be shown that Chef cannot choose two numbers among $8$, $4$ and $6$ with odd sum.
"""

def can_choose_two_with_odd_sum(A, B, C):
    # Check if any two numbers have an odd sum
    if (A + B) % 2 == 1 or (A + C) % 2 == 1 or (B + C) % 2 == 1:
        return "YES"
    else:
        return "NO"