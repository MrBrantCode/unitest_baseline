"""
QUESTION:
Find T(n), where T(n) = ∑ r_X + r_Y + r_Z + r_W, given that circles X, Y, and Z are tangent to each other and to line M at four distinct points, and circle W is inside the space between X, Y, Z, and M, and tangent to all four. The radii r_X, r_Y, r_Z, and r_W are integers and 0 < r_X ≤ r_Y ≤ r_Z ≤ n.
"""

def T(n):
    total_sum = 0
    for r_y in range(1, n+1):
        for r_x in range(1, r_y+1):
            for r_z in range(r_y, n+1):
                r_w_numerator = (r_x*r_y + r_y*r_z + r_z*r_x) * (n+1)
                r_w_denominator = r_x + r_y + r_z
                if r_w_numerator % r_w_denominator == 0:
                    r_w = r_w_numerator // r_w_denominator - 1
                    if r_w >= 0 and r_w <= n:
                        total_sum += r_x + r_y + r_z + r_w
    return total_sum