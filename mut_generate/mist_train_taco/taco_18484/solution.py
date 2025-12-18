"""
QUESTION:
There is a white sheet of paper lying on a rectangle table. The sheet is a rectangle with its sides parallel to the sides of the table. If you will take a look from above and assume that the bottom left corner of the table has coordinates $(0, 0)$, and coordinate axes are left and bottom sides of the table, then the bottom left corner of the white sheet has coordinates $(x_1, y_1)$, and the top right — $(x_2, y_2)$.

After that two black sheets of paper are placed on the table. Sides of both black sheets are also parallel to the sides of the table. Coordinates of the bottom left corner of the first black sheet are $(x_3, y_3)$, and the top right — $(x_4, y_4)$. Coordinates of the bottom left corner of the second black sheet are $(x_5, y_5)$, and the top right — $(x_6, y_6)$.  [Image] Example of three rectangles. 

Determine if some part of the white sheet can be seen from the above after the two black sheets are placed. The part of the white sheet can be seen if there is at least one point lying not strictly inside the white sheet and strictly outside of both black sheets.


-----Input-----

The first line of the input contains four integers $x_1, y_1, x_2, y_2$ $(0 \le x_1 < x_2 \le 10^{6}, 0 \le y_1 < y_2 \le 10^{6})$ — coordinates of the bottom left and the top right corners of the white sheet.

The second line of the input contains four integers $x_3, y_3, x_4, y_4$ $(0 \le x_3 < x_4 \le 10^{6}, 0 \le y_3 < y_4 \le 10^{6})$ — coordinates of the bottom left and the top right corners of the first black sheet.

The third line of the input contains four integers $x_5, y_5, x_6, y_6$ $(0 \le x_5 < x_6 \le 10^{6}, 0 \le y_5 < y_6 \le 10^{6})$ — coordinates of the bottom left and the top right corners of the second black sheet.

The sides of each sheet of paper are parallel (perpendicular) to the coordinate axes.


-----Output-----

If some part of the white sheet can be seen from the above after the two black sheets are placed, print "YES" (without quotes). Otherwise print "NO".


-----Examples-----
Input
2 2 4 4
1 1 3 5
3 1 5 5

Output
NO

Input
3 3 7 5
0 0 4 6
0 0 7 4

Output
YES

Input
5 2 10 5
3 1 7 6
8 1 11 7

Output
YES

Input
0 0 1000000 1000000
0 0 499999 1000000
500000 0 1000000 1000000

Output
YES



-----Note-----

In the first example the white sheet is fully covered by black sheets.

In the second example the part of the white sheet can be seen after two black sheets are placed. For example, the point $(6.5, 4.5)$ lies not strictly inside the white sheet and lies strictly outside of both black sheets.
"""

def can_see_white_sheet(white, black1, black2):
    """
    Determines if some part of the white sheet can be seen from above after the two black sheets are placed.

    Parameters:
    white (tuple): A tuple of four integers (x1, y1, x2, y2) representing the coordinates of the bottom left and top right corners of the white sheet.
    black1 (tuple): A tuple of four integers (x3, y3, x4, y4) representing the coordinates of the bottom left and top right corners of the first black sheet.
    black2 (tuple): A tuple of four integers (x5, y5, x6, y6) representing the coordinates of the bottom left and top right corners of the second black sheet.

    Returns:
    bool: True if some part of the white sheet can be seen, False otherwise.
    """
    
    def intersection(A, B):
        return (max(A[0], B[0]), max(A[1], B[1]), min(A[2], B[2]), min(A[3], B[3]))

    def area(A):
        return max(A[2] - A[0], 0) * max(A[3] - A[1], 0)

    white_area = area(white)
    intersection_with_black1 = area(intersection(white, black1))
    intersection_with_black2 = area(intersection(white, black2))
    intersection_with_both_blacks = area(intersection(white, intersection(black1, black2)))

    if intersection_with_black1 + intersection_with_black2 - intersection_with_both_blacks == white_area:
        return False
    else:
        return True