"""
QUESTION:
Chef has X 5 rupee coins and Y 10 rupee coins. Chef goes to a shop to buy chocolates for Chefina where each chocolate costs Z rupees. Find the maximum number of chocolates that Chef can buy for Chefina.

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers X, Y and Z — the number of 5 rupee coins, the number of 10 rupee coins and the cost of each chocolate.

------ Output Format ------ 

For each test case, output the maximum number of chocolates that Chef can buy for Chefina.

------ Constraints ------ 

$1 ≤ T ≤ 100$ 
$1 ≤ X,Y,Z ≤ 1000$

----- Sample Input 1 ------ 
4
10 10 10
3 1 8
8 1 3
4 4 1000
----- Sample Output 1 ------ 
15
3
16
0

----- explanation 1 ------ 
Test case $1$: Chef has $10 \cdot 5 + 10 \cdot 10 = 150$ rupees in total. Since each chocolate costs $10$ rupees, Chef can spend all $150$ rupees and buy $15$ chocolates for Chefina.

Test case $2$: Chef has $3 \cdot 5 + 1 \cdot 10 = 25$ rupees in total. Since each chocolate costs $8$ rupees, Chef can buy a maximum of $3$ chocolates for Chefina, leaving him with $1$ rupee.

Test case $3$: Chef has $8 \cdot 5 + 1 \cdot 10 = 50$ rupees in total. Since each chocolate costs $3$ rupees, Chef can buy a maximum of $16$ chocolates for Chefina, leaving him with $2$ rupee.

Test case $4$: Chef has $4 \cdot 5 + 4 \cdot 10 = 60$ rupees in total. Since each chocolate costs $1000$ rupees, Chef can buy no chocolate for Chefina, leaving him with $60$ rupees.
"""

def calculate_max_chocolates(X: int, Y: int, Z: int) -> int:
    """
    Calculate the maximum number of chocolates Chef can buy with the given number of 5 rupee and 10 rupee coins.

    Parameters:
    X (int): Number of 5 rupee coins.
    Y (int): Number of 10 rupee coins.
    Z (int): Cost of each chocolate.

    Returns:
    int: The maximum number of chocolates Chef can buy.
    """
    total_money = X * 5 + Y * 10
    return total_money // Z