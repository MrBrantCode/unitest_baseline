"""
QUESTION:
Victor is building a Japanese rock garden in his $24\times24$ square courtyard. He overlaid the courtyard with a Cartesian coordinate system so that any point $(x,y)$ in the courtyard has coordinates $x\in[-12,12]$ and $y\in[-12,12]$. Victor wants to place $12$ stones in the garden according to the following rules:

The center of each stone is located at some point $(x,y)$, where $\boldsymbol{x}$ and $y$ are integers $\in[-12,12]$. 
The coordinates of all twelve stones are pairwise distinct. 
The Euclidean distance from the center of any stone to the origin is not an integer. 
The sum of Euclidean distances between all twelve points and the origin is an almost integer, meaning the absolute difference between this sum and an integer must be $\leq10^{-12}$.

Given the values of $\boldsymbol{x}$ and $y$ for the first stone Victor placed in the garden, place the remaining $\mbox{11}$ stones according to the requirements above. For each stone you place, print two space-separated integers on a new line describing the respective $\boldsymbol{x}$ and $y$ coordinates of the stone's location.

Input Format

Two space-separated integers describing the respective values of $\boldsymbol{x}$ and $y$ for the first stone's location.

Constraints

$-12\leq x,y\leq12$

Output Format

Print $\mbox{11}$ lines, where each line contains two space-separated integers describing the respective values of $\boldsymbol{x}$ and $y$ for a stone's location.

Sample Input 0
7 11

Sample Output 0
11 1
-2 12
5 4
12 -3
10 3
9 6
-12 -7
1 11
-6 -6
12 -4
4 12

Explanation 0

The diagram below depicts the placement of each stone and maps its distance to the origin (note that red denotes the first stone placed by Victor and blue denotes the eleven remaining stones we placed):

Now, let's determine if the sum of these distances is an almost integer. First, we find the distance from the origin to the stone Victor placed at $(7,11)$, which is $\sqrt{7^2+11^2}\approx13.038404810405297429165943114858$. Next, we calculate the distances for the remaining stones we placed in the graph above:

$\sqrt{11^2+1^2}\approx11.045361017187260774210913843344$
$\sqrt{(-2)^2+12^2}\approx12.165525060596439377999368490404\text{}$
$\sqrt{5^2+4^2}\approx6.4031242374328486864882176746218$
$\sqrt{12^2+(-3)^2}\approx12.36931687652981649464229567922$
$\sqrt{10^2+3^2}\approx10.44060650891055017975754022548\text{}$
$\sqrt{9^2+6^2}\approx10.816653826391967879357663802411$
$\sqrt{(-12)^2+(-7)^2}\approx13.89243989449804508432547041029\text{}$
$\sqrt{1^2+11^2}\approx11.045361017187260774210913843344$
$\sqrt{(-6)^2+(-6)^2}\approx8.4852813742385702928101323452582$
$\sqrt{12^2+(-4)^2}\approx12.649110640673517327995574177731$
$\sqrt{4^2+12^2}\approx12.64911064067351737995574177731$

When we sum these eleven distances with the distance for the stone Victor placed, we get $\approx135.000000000000016207888321012$. The nearest integer to this number is $135$, and the distance between this sum and the nearest integer is $\approx1.6\times10^{-14}\leq10^{-12}$ (meaning it's an almost integer). Because this configuration satisfies all of Victor's rules for his rock garden, we print eleven lines of x y coordinates describing the locations of the stones we placed.
"""

def find_remaining_stones(first_stone_x: int, first_stone_y: int) -> list:
    import math

    # Predefined solutions
    solutions = [
        {(7, 11), (11, 1), (-2, 12), (5, 4), (12, -3), (10, 3), (9, 6), (-12, -7), (1, 11), (-6, -6), (12, -4), (4, 12)},
        {(-12, 8), (9, -6), (10, 5), (-5, 1), (3, 3), (3, 1), (-10, -2), (2, 1), (7, 5), (2, 2), (6, 5), (9, 7)},
        {(10, 5), (-2, 1), (3, 3), (3, 1), (10, 2), (-7, -5), (12, 8), (2, 2), (6, -5), (5, 1), (-9, 6), (9, 7)},
        {(10, 2), (-2, 2), (12, 6), (3, -1), (-11, 3), (-7, -5), (2, 2), (5, 1), (9, 6), (1, 1), (6, 5), (12, 8)},
        {(9, 7), (3, 2), (-10, 2), (-5, 1), (7, 1), (7, -5), (3, 1), (-9, -6), (4, 2), (9, 6), (6, 5), (8, 4)},
        {(7, 3), (-12, -7), (6, -3), (11, 5), (12, 7), (9, 3), (7, 7), (-12, 7), (-3, 2), (10, 1), (4, 2), (9, 7)},
        {(7, 3), (10, 8), (-5, 1), (11, 4), (9, 1), (10, 6), (-11, -2), (12, 11), (6, -6), (12, 10), (-11, 7), (10, 9)},
        {(9, 7), (-9, -1), (12, 7), (-10, 4), (-3, 1), (11, 1), (12, 8), (8, -4), (12, 10), (10, 3), (1, 1), (5, 3)},
        {(11, 7), (3, 2), (10, 8), (11, 4), (9, 2), (-11, 1), (11, 2), (-7, 6), (-11, -1), (10, -8), (10, 1), (12, 11)},
        {(10, 8), (8, 3), (10, 5), (8, 1), (10, 6), (12, 6), (-11, 8), (-10, 5), (11, -5), (10, 3), (-11, -8), (12, 8)},
        {(12, 2), (8, 3), (-4, 4), (10, 4), (8, 1), (-10, -5), (10, 6), (9, 3), (7, 5), (-12, 8), (7, -4), (5, 2)},
        {(-9, 4), (11, 4), (12, 1), (8, 2), (7, 1), (-10, -8), (3, 1), (9, -4), (12, 4), (9, 4), (-12, 4), (4, 1)},
        {(10, 8), (12, 1), (11, 4), (5, 5), (-9, -4), (3, 1), (9, -4), (-6, 2), (6, 2), (9, 4), (-12, 4), (12, 3)},
        {(9, 7), (-12, 12), (-9, 5), (6, 1), (10, 6), (-10, -6), (9, -9), (8, 7), (9, 4), (8, 5), (10, 9), (5, 3)},
        {(-9, 4), (10, 10), (6, 1), (10, 6), (-11, -3), (10, -6), (8, 7), (-11, 11), (9, 5), (8, 5), (10, 9), (5, 3)},
        {(6, 4), (9, 7), (5, 5), (3, 1), (3, -2), (-7, -5), (-3, 2), (-12, 6), (5, 1), (9, 6), (6, 5), (10, 2)},
        {(8, -7), (3, 2), (5, 1), (-9, -1), (10, 7), (9, 2), (-7, 5), (11, 3), (-11, 4), (6, 2), (12, 10), (11, 6)},
        {(11, 4), (8, 2), (-12, -10), (11, 8), (8, 1), (9, 8), (9, 9), (-12, 10), (-7, 2), (12, -10), (11, 6), (8, 4)},
        {(10, 8), (12, 1), (9, 1), (7, 6), (9, 3), (11, 9), (2, 1), (-12, 11), (9, -4), (12, 11), (-6, 6), (-10, -1)},
        {(7, 3), (11, 10), (11, 5), (10, 7), (-8, -5), (-8, 5), (11, 3), (8, -5), (7, 5), (9, 5), (-9, 6), (6, 5)},
        {(12, 2), (9, 2), (10, 7), (-9, -4), (11, 9), (10, 6), (-12, 11), (9, -3), (8, 8), (11, 1), (-7, 2), (7, 2)}
    ]

    # Generate additional solutions by reflecting the coordinates
    solutions2 = []
    for sol in solutions:
        solutions2.append(list(map(lambda p: (p[0], -p[1]), sol)))
    solutions += solutions2
    solutions2 = []
    for sol in solutions:
        solutions2.append(list(map(lambda p: (-p[0], p[1]), sol)))
    solutions += solutions2
    solutions2 = []
    for sol in solutions:
        solutions2.append(list(map(lambda p: (p[1], p[0]), sol)))
    solutions += solutions2

    # Find the solution that contains the first stone
    for sol in solutions:
        if (first_stone_x, first_stone_y) in sol:
            remaining_stones = [p for p in sol if p != (first_stone_x, first_stone_y)]
            return remaining_stones

    # If no solution is found, return an empty list (though this should not happen with valid input)
    return []