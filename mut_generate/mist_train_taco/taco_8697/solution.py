"""
QUESTION:
Chef and Chefina are residing in a hotel.

There are 10 floors in the hotel and each floor consists of 10 rooms.

Floor 1 consists of room numbers 1 to 10.
Floor 2 consists of room numbers 11 to 20.  
\ldots
Floor i consists of room numbers 10 \cdot (i-1) + 1 to 10 \cdot i.

You know that Chef's room number is X while Chefina's Room number is Y.  
If Chef starts from his room, find the number of floors he needs to travel to reach Chefina's room.

------ Input Format ------ 

- First line will contain T, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers X, Y, the room numbers of Chef and Chefina respectively.

------ Output Format ------ 

For each test case, output the number of floors Chef needs to travel to reach Chefina's room.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ X, Y ≤ 100$
$X \neq Y$

----- Sample Input 1 ------ 
4
1 100
42 50
53 30
81 80

----- Sample Output 1 ------ 
9
0
3
1

----- explanation 1 ------ 
Test Case $1$: Since Room $1$ is on $1^{st}$ floor and Room $100$ is on $10^{th}$ floor, Chef needs to climb $9$ floors to reach Chefina's Room.

Test Case $2$: Since Room $42$ is on $5^{th}$ floor and Room $50$ is also on $5^{th}$ floor, Chef does not need to climb any floor.

Test Case $3$: Since Room $53$ is on $6^{th}$ floor and Room $30$ is on $3^{rd}$ floor, Chef needs to go down $3$ floors to reach Chefina's Room.

Test Case $4$: Since Room $81$ is on $9^{th}$ floor and Room $80$ is on $8^{th}$ floor, Chef needs to go down $1$ floors to reach Chefina's Room.
"""

import math

def calculate_floor_difference(X: int, Y: int) -> int:
    """
    Calculate the number of floors Chef needs to travel to reach Chefina's room.

    Parameters:
    - X (int): The room number of Chef.
    - Y (int): The room number of Chefina.

    Returns:
    - int: The number of floors Chef needs to travel.
    """
    floor_X = math.ceil(X / 10)
    floor_Y = math.ceil(Y / 10)
    return abs(floor_X - floor_Y)