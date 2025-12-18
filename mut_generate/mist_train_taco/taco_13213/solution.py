"""
QUESTION:
Find max number of squares (S) of side 2 units that can fit in an Isosceles triangle with a right angle and its shortest side equal to "B" units.
Note: The squares don't have to fit completely inside the Triangle.
 
Example 1:
Input:
B = 1
Output:
0
Explanation:
We can't fit any squares.
Example 2:
Input:
B = 10
Output:
10
Explanation:
We can fit 10 squares of 2 unit sides
in an Isosceles Right Traingle with
the shortest side being 10 unit length.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxSquares() which takes an Integer B as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= B <= 10^{9}
"""

def max_squares_in_triangle(B: int) -> int:
    """
    Calculate the maximum number of 2x2 squares that can fit in an isosceles right triangle
    with the shortest side equal to B units.

    Parameters:
    B (int): The length of the shortest side of the isosceles right triangle.

    Returns:
    int: The maximum number of 2x2 squares that can fit in the triangle.
    """
    s = B // 2
    return s * (s - 1) // 2