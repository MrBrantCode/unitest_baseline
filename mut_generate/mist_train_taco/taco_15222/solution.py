"""
QUESTION:
Chef has a rectangular plate of length  N cm  and width M cm. He wants to make a wireframe around the plate. The wireframe costs X rupees per cm. 

Determine the cost Chef needs to incur to buy the wireframe.

------ Input Format ------ 

- First line will contain T, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing three space-separated integers N,M, and X — the length of the plate, width of the plate, and the cost of frame per cm.

------ Output Format ------ 

For each test case, output in a single line, the price Chef needs to pay for the wireframe.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ N,M,X ≤ 1000 $

----- Sample Input 1 ------ 
3
10 10 10
23 3 12
1000 1000 1000

----- Sample Output 1 ------ 
400
624
4000000
----- explanation 1 ------ 
Test case $1$: The total length of the frame is $2\cdot 10 + 2\cdot 10 = 40$ cms. Since the cost is $10$ per cm, the total cost would be $10 \cdot 40 = 400$.

Test case $2$: The total length of the frame is $2\cdot 23 + 2\cdot 3 = 52$ cms. Since the cost is $12$ per cm, the total cost would be $52 \cdot 12 = 624$.

Test case $3$: The total length of the frame is $2\cdot 1000 + 2\cdot 1000 = 4000$ cms. Since the cost is $1000$ per cm, the total cost would be $4000 \cdot 1000 = 4000000$.
"""

def calculate_wireframe_cost(N: int, M: int, X: int) -> int:
    """
    Calculate the cost Chef needs to incur to buy the wireframe for a rectangular plate.

    Parameters:
    - N (int): The length of the plate in cm.
    - M (int): The width of the plate in cm.
    - X (int): The cost per cm of the wireframe in rupees.

    Returns:
    - int: The total cost in rupees.
    """
    perimeter = 2 * (N + M)
    cost = perimeter * X
    return cost