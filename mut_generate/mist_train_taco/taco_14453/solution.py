"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Chef likes problems on geometry a lot. Please help him to solve one such problem.

Find all possible triangles with integer sides which has the radius of inscribed circle (also known as incircle) equal to R.

Two triangles are said to be different if they have at least one different side lengths. Formally, let there be two triangles T_{1}, T_{2}. Let a, b, c denote the sides of triangle T_{1}, such that a ≤ b ≤ c. Similarly, Let d, e, f denote the sides of triangle T_{2}, such that d ≤ e ≤ f. Then T_{1} will said to be different from T_{2} if either a ≠ d, or b ≠ e or c ≠ f.

------ Input ------ 

There is a single test case per test file.
The only line of input contains an integer R.

------ Output ------ 

Output in first line single number - number of triangles satisfying statement.
Order the sides of triangles in non-decreasing order. Output all triangles in non-decreasing order, i.e. order first by smallest sides, otherwise by second smallest sides, if first and second sides equal, then by third.

------ Constraints ------ 

$1 ≤ R ≤ 100 $

------ Subtasks ------ 

$Subtask #1: (20 points)  1 ≤ R ≤ 3$
$Subtask #2: (30 points)  1 ≤ R ≤ 20$
$Subtask #3: (50 points)  Original constraints$

------ Example ------ 

Input:
2

Output:
5
5 12 13
6 8 10
6 25 29
7 15 20
9 10 17
"""

def find_integer_triangles_with_incircle_radius(R):
    """
    Finds all possible triangles with integer sides which have the radius of the inscribed circle (incircle) equal to R.

    Parameters:
    R (int): The radius of the inscribed circle.

    Returns:
    tuple: A tuple containing:
           - int: The number of triangles.
           - list: A list of lists, where each inner list contains the sides of a triangle in non-decreasing order.
    """
    t = 4 * R * R
    ans = []
    z = 1
    while z * z <= 3 * t:
        y = z
        while True:
            nom = (y + z) * t
            denom = y * z - t
            if nom < y * denom:
                break
            if denom > 0 and nom % denom == 0:
                x = nom // denom
                if x % 2 == y % 2 and x % 2 == z % 2:
                    a = (y + z) // 2
                    b = (x + z) // 2
                    c = (x + y) // 2
                    ans.append([a, b, c])
            y += 1
        z += 1
    ans.sort()
    return len(ans), ans