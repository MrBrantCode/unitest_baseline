"""
QUESTION:
Chef has a bucket having a capacity of K liters. It is already filled with X liters of water. 

Find the maximum amount of extra water in liters that Chef can fill in the bucket without overflowing.  

------ Input Format ------ 

- The first line will contain T - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space separated integers K and X - as mentioned in the problem.

------ Output Format ------ 

For each test case, output in a single line, the amount of extra water in liters that Chef can fill in the bucket without overflowing.  

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ X < K ≤ 1000$

----- Sample Input 1 ------ 
2
5 4
15 6

----- Sample Output 1 ------ 
1
9

----- explanation 1 ------ 
Test Case $1$: The capacity of the bucket is $5$ liters but it is already filled with $4$ liters of water. Adding $1$ more liter of water to the bucket fills it to $(4+1) = 5$ liters. If we try to fill more water, it will overflow.

Test Case $2$: The capacity of the bucket is $15$ liters but it is already filled with $6$ liters of water. Adding $9$ more liters of water to the bucket fills it to $(6+9) = 15$ liters. If we try to fill more water, it will overflow.
"""

def calculate_extra_water(K: int, X: int) -> int:
    """
    Calculate the maximum amount of extra water that can be added to the bucket without overflowing.

    Parameters:
    - K (int): The capacity of the bucket in liters.
    - X (int): The amount of water already in the bucket in liters.

    Returns:
    - int: The maximum amount of extra water in liters that can be added to the bucket without overflowing.
    """
    return K - X