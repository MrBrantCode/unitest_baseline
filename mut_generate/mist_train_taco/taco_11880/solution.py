"""
QUESTION:
You are given that a mango weighs X kilograms and a truck weighs Y kilograms.
You want to cross a bridge that can withstand a weight of Z kilograms. 

Find the maximum number of mangoes you can load in the truck so that you can cross the bridge safely.

------ Input Format ------ 

- First line will contain T, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, three integers X, Y, Z - the weight of mango, the weight of truck and the weight the bridge can withstand respectively.

------ Output Format ------ 

For each test case, output in a single line the maximum number of mangoes that you can load in the truck.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ X ≤ Y ≤ Z ≤ 100$

----- Sample Input 1 ------ 
4
2 5 11
4 10 20
1 1 1
6 40 90

----- Sample Output 1 ------ 
3
2
0
8

----- explanation 1 ------ 
Test case $1$: You can load $3$ mangoes at maximum. The total weight is $ 3\times 2+5 = 11 ≤ 11$. Thus, the truck can safely cross the bridge with $3$ mangoes. If you load $4$ mangoes, the total weight is $4\times 2+5 = 13 > 11$. 

Test case $2$: You can load $2$ mangoes at maximum. The total weight is $ 2\times 4+10 = 18 ≤ 20$. Thus, the truck can safely cross the bridge with $2$ mangoes.

Test case $3$: You can load $0$ mangoes at maximum. The total weight is $ 0\times 1+1 = 1 ≤ 1$. Thus, the truck can safely cross the bridge only if there are $0$ mangoes.

Test case $4$: You can load $8$ mangoes at maximum. The total weight is $ 6\times 8+40 = 88 ≤ 90$. Thus, the truck can safely cross the bridge with $8$ mangoes.
"""

def calculate_max_mangoes(x: int, y: int, z: int) -> int:
    """
    Calculate the maximum number of mangoes that can be loaded in the truck
    without exceeding the bridge's weight limit.

    Parameters:
    - x (int): The weight of a single mango.
    - y (int): The weight of the truck.
    - z (int): The maximum weight the bridge can withstand.

    Returns:
    - int: The maximum number of mangoes that can be loaded in the truck.
    """
    # Calculate the maximum weight that can be added to the truck
    max_additional_weight = z - y
    
    # Calculate the maximum number of mangoes that can be loaded
    max_mangoes = max_additional_weight // x
    
    return max_mangoes