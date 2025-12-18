"""
QUESTION:
The Chessboard Distance for any two points (X_{1}, Y_{1}) and (X_{2}, Y_{2}) on a Cartesian plane is defined as max(|X_{1} - X_{2}|, |Y_{1} - Y_{2}|). 

You are given two points (X_{1}, Y_{1}) and (X_{2}, Y_{2}). Output their Chessboard Distance. 

Note that, |P| denotes the absolute value of integer P. For example, |-4| = 4 and |7| = 7.

------ Input Format ------ 

- First line will contain T, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input containing 4 space separated integers - X_{1}, Y_{1}, X_{2}, Y_{2} - as defined in the problem statement.

------ Output Format ------ 

For each test case, output in a single line the chessboard distance between (X_{1}, Y_{1}) and (X_{2}, Y_{2})

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ X_{1}, Y_{1}, X_{2}, Y_{2} ≤ 10^{5}$

------ subtasks ------ 

Subtask #1 (100 points): original constraints

----- Sample Input 1 ------ 
3
2 4 5 1
5 5 5 3
1 4 3 3

----- Sample Output 1 ------ 
3
2
2

----- explanation 1 ------ 
- In the first case, the distance between $(2, 4)$ and $(5, 1)$ is $max(|2- 5|, |4 - 1|) = max(|-3|, |3|) = 3$.

- In the second case, the distance between $(5, 5)$ and $(5, 3)$ is $max(|5- 5|, |5 - 3|) = max(|0|, |2|) = 2$.

- In the third case, the distance between $(1, 4)$ and $(3, 3)$ is $max(|1- 3|, |4 - 3|) = max(|-2|, |1|) = 2$.
"""

def calculate_chessboard_distance(X1: int, Y1: int, X2: int, Y2: int) -> int:
    """
    Calculate the chessboard distance between two points (X1, Y1) and (X2, Y2) on a Cartesian plane.

    The chessboard distance is defined as max(|X1 - X2|, |Y1 - Y2|).

    Parameters:
    - X1 (int): The x-coordinate of the first point.
    - Y1 (int): The y-coordinate of the first point.
    - X2 (int): The x-coordinate of the second point.
    - Y2 (int): The y-coordinate of the second point.

    Returns:
    - int: The chessboard distance between the two points.
    """
    return max(abs(X1 - X2), abs(Y1 - Y2))