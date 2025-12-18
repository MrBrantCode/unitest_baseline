"""
QUESTION:
Chef is fond of burgers and decided to make as many burgers as possible.

Chef has A patties and B buns. To make 1 burger, Chef needs 1 patty and 1 bun.  
Find the maximum number of burgers that Chef can make.

------ Input Format ------ 

- The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
- The first and only line of each test case contains two space-separated integers A and B, the number of patties and buns respectively.

------ Output Format ------ 

For each test case, output the maximum number of burgers that Chef can make. 

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ A, B ≤ 10^{5}$

----- Sample Input 1 ------ 
4
2 2
2 3
3 2
23 17
----- Sample Output 1 ------ 
2
2
2
17

----- explanation 1 ------ 
Test case $1$: Chef has $2$ patties and $2$ buns, and therefore Chef can make $2$ burgers.

Test case $2$: Chef has $2$ patties and $3$ buns. Chef can make at most $2$ burgers by using $2$ patties and $2$ buns.

Test case $3$: Chef has $3$ patties and $2$ buns. Chef can make at most $2$ burgers by using $2$ patties and $2$ buns.

Test case $4$: Chef has $23$ patties and $17$ buns. Chef can make at most $17$ burgers by using $17$ patties and $17$ buns.
"""

def max_burgers(A: int, B: int) -> int:
    """
    Calculate the maximum number of burgers that can be made with the given number of patties and buns.

    Parameters:
    - A (int): Number of patties.
    - B (int): Number of buns.

    Returns:
    - int: The maximum number of burgers that can be made.
    """
    return min(A, B)