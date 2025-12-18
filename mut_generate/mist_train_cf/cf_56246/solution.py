"""
QUESTION:
Find the function `T(n)` where `T(n)` is the sum of the radii of circles `P`, `Q`, `R`, and `S` that are tangent to each other and to line `M`, where `r_P`, `r_Q`, `r_R`, and `r_S` are integers and `0 < r_P <= r_Q <= r_R <= n`. The configuration of radii follows the pattern `x^2`, `x^2`, `xy`, and `y^2` for some integers `x` and `y` where `x > y`.
"""

def T(n):
    total = 0
    x = 1
    while x * x < n:
        y = 1
        while y <= x:
            if x * x + x * y + y * y <= n:
                if y < x:
                    total += 2 * (x * x + x * y + y * y)
                else:
                    total += x * x + x * y + y * y
            y += 1
        x += 1
    return total