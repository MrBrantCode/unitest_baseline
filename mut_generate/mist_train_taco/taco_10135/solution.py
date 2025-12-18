"""
QUESTION:
Chef has invented 1-minute Instant Noodles. As the name suggests, each packet takes exactly 1 minute to cook.

Chef's restaurant has X stoves and only 1 packet can be cooked in a single pan. 

How many customers can Chef serve in Y minutes if each customer orders exactly 1 packet of noodles?

------ Input Format ------ 

- The first and only line of input contains two space-separated integers X and Y — the number of stoves and the number of minutes, respectively.

------ Output Format ------ 

- Print a single integer, the maximum number of customers Chef can serve in Y minutes

------ Constraints ------ 

$1 ≤ X, Y ≤ 1000$

----- Sample Input 1 ------ 
3 7
----- Sample Output 1 ------ 
21
----- explanation 1 ------ 

Chef cooks for $Y = 7$ minutes and can cook $X = 3$ packets per minute, one on each stove.

So, the total number of packets that can be cooked is $X \cdot Y = 3 \cdot 7 = 21$. 

Each person orders one packet, so the maximum number of customers that can be served is $21$.

----- Sample Input 2 ------ 
7 8
----- Sample Output 2 ------ 
56
----- explanation 2 ------ 

Chef cooks for $Y = 8$ minutes and can cook $X = 7$ packets per minute, one on each stove.

So, the total number of packets that can be cooked is $X \cdot Y = 7 \cdot 8 = 56$. 

Each person orders one packet, so the maximum number of customers that can be served is $56$.
"""

def calculate_max_customers(X: int, Y: int) -> int:
    """
    Calculate the maximum number of customers that can be served in Y minutes with X stoves.

    Parameters:
    - X (int): Number of stoves.
    - Y (int): Number of minutes.

    Returns:
    - int: Maximum number of customers that can be served.
    """
    return X * Y