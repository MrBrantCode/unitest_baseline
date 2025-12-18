"""
QUESTION:
# Task
 Consider a `bishop`, a `knight` and a `rook` on an `n × m` chessboard. They are said to form a `triangle` if each piece attacks exactly one other piece and is attacked by exactly one piece. 
 
 Calculate the number of ways to choose positions of the pieces to form a triangle.

 Note that the bishop attacks pieces sharing the common diagonal with it; the rook attacks in horizontal and vertical directions; and, finally, the knight attacks squares which are two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from its position.

 ![](https://codefightsuserpics.s3.amazonaws.com/tasks/chessTriangle/img/moves.png?_tm=1473934712872)

# Example

 For `n = 2 and m = 3`, the output should be `8`.

 ![](https://codefightsuserpics.s3.amazonaws.com/tasks/chessTriangle/img/combinations.png?_tm=1473934713038)

# Input/Output


- `[input]` integer `n`

    Constraints: `1 ≤ n ≤ 40.`


 - `[input]` integer `m`

    Constraints: `1 ≤ m ≤ 40, 3 ≤ n x m`.


 - `[output]` an integer
"""

def count_chess_triangle_ways(n, m):
    # Define the dimensions for which we need to calculate the number of ways
    dimensions = [(3, 4), (3, 3), (2, 4), (2, 3)]
    
    # Initialize the total count of ways
    total_ways = 0
    
    # Iterate over each dimension
    for dim in dimensions:
        x, y = dim
        # Check if the dimension fits within the board size
        if x <= n and y <= m:
            # Calculate the number of ways for this dimension
            ways = 8 * (n - x + 1) * (m - y + 1)
            # Add to the total count
            total_ways += ways
    
    return total_ways