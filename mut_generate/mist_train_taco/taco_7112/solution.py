"""
QUESTION:
Determine if an N-sided polygon (not necessarily convex) with sides of length L_1, L_2, ..., L_N can be drawn in a two-dimensional plane.
You can use the following theorem:
Theorem: an N-sided polygon satisfying the condition can be drawn if and only if the longest side is strictly shorter than the sum of the lengths of the other N-1 sides.

-----Constraints-----
 - All values in input are integers.
 - 3 \leq N \leq 10
 - 1 \leq L_i \leq 100

-----Input-----
Input is given from Standard Input in the following format:
N
L_1 L_2 ... L_N

-----Output-----
If an N-sided polygon satisfying the condition can be drawn, print Yes; otherwise, print No.

-----Sample Input-----
4
3 8 5 1

-----Sample Output-----
Yes

Since 8 < 9 = 3 + 5 + 1, it follows from the theorem that such a polygon can be drawn on a plane.
"""

def can_draw_polygon(N, sides):
    # Ensure the number of sides matches the input length
    if len(sides) != N:
        raise ValueError("The number of sides does not match the input length.")
    
    # Find the maximum side length
    max_side = max(sides)
    
    # Calculate the sum of the other sides
    sum_other_sides = sum(sides) - max_side
    
    # Check the condition for drawing the polygon
    if max_side < sum_other_sides:
        return "Yes"
    else:
        return "No"