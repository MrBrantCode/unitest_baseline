"""
QUESTION:
Chef is given two integers A and C such that A ≤ C. 

Chef wants to find whether there exists any integer B such that A, B, and C are in [arithmetic progression].

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two space-separated integers A and C, the given integers.

------ Output Format ------ 

For each test case, output -1 if there exists no integer B such that A, B, and C are in arithmetic progression. Else, output the value of B.

------ Constraints ------ 

$1 ≤ T ≤ 60$
$1 ≤ A ≤ C ≤ 10$

----- Sample Input 1 ------ 
4
3 5
6 6
2 7
1 9

----- Sample Output 1 ------ 
4
6
-1
5

----- explanation 1 ------ 
Test case $1$: Considering $B = 4$, the three integers are in arithmetic progression as $B-A = C-B = 1$.

Test case $2$: Considering $B = 6$, the three integers are in arithmetic progression as $B-A = C-B = 0$.

Test case $3$: There exists no integral value of $B$ such that $A, B, $ and $C$ are in arithmetic progression.

Test case $4$: Considering $B = 5$, the three integers are in arithmetic progression as $B-A = C-B = 4$.
"""

def find_arithmetic_progression_B(A: int, C: int) -> int:
    k = A + C
    if k % 2 == 0:
        return int(k / 2)
    else:
        return -1