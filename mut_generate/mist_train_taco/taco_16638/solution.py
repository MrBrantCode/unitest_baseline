"""
QUESTION:
Chef is given three numbers A, B, and C.

He wants to find whether he can select exactly two numbers out of these such that the product of the selected numbers is negative.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of three integers A, B, and C, the given numbers.

------ Output Format ------ 

For each test case, output YES if Chef can select exactly two numbers out of these such that the product of the selected numbers is negative, NO otherwise.

You may print each character in uppercase or lowercase. For example, the strings NO, no, No, and nO, are all considered identical.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$-10 ≤ A, B, C ≤ 10$

----- Sample Input 1 ------ 
5
1 5 7
-5 0 4
6 -1 0
-3 -5 -2
0 0 -4

----- Sample Output 1 ------ 
NO
YES
YES
NO
NO

----- explanation 1 ------ 
Test case $1$: There exists no way to select two numbers such that their product is negative.

Test case $2$: The product of $-5$ and $4$ is $-5\cdot 4 = -20$ which is negative.

Test case $3$: The product of $6$ and $-1$ is $6\cdot (-1) = -6$ which is negative.

Test case $4$: There exists no way to select two numbers such that their product is negative.

Test case $5$: There exists no way to select two numbers such that their product is negative.
"""

def can_select_two_for_negative_product(a: int, b: int, c: int) -> str:
    if a * b < 0 or b * c < 0 or c * a < 0:
        return "YES"
    else:
        return "NO"