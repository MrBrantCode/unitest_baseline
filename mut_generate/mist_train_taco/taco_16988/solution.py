"""
QUESTION:
The Department of economic development of IT City created a model of city development till year 2100.

To prepare report about growth perspectives it is required to get growth estimates from the model.

To get the growth estimates it is required to solve a quadratic equation. Since the Department of economic development of IT City creates realistic models only, that quadratic equation has a solution, moreover there are exactly two different real roots.

The greater of these roots corresponds to the optimistic scenario, the smaller one corresponds to the pessimistic one. Help to get these estimates, first the optimistic, then the pessimistic one.


-----Input-----

The only line of the input contains three integers a, b, c ( - 1000 ≤ a, b, c ≤ 1000) — the coefficients of ax^2 + bx + c = 0 equation.


-----Output-----

In the first line output the greater of the equation roots, in the second line output the smaller one. Absolute or relative error should not be greater than 10^{ - 6}.


-----Examples-----
Input
1 30 200

Output
-10.000000000000000
-20.000000000000000
"""

def solve_quadratic_equation(a: int, b: int, c: int) -> tuple:
    # Calculate the discriminant
    d = b ** 2 - 4 * a * c
    
    # Handle special cases
    if a == 0 and c == 0:
        return (0.0, 0.0)
    elif a == 0:
        ans = -1 * c / b
        return (ans, ans)
    elif d == 0:
        ans = -1 * b / (2 * a)
        return (ans, ans)
    else:
        # Calculate the roots
        root1 = (-b + d ** 0.5) / (2 * a)
        root2 = (-b - d ** 0.5) / (2 * a)
        
        # Ensure the roots are returned in the correct order
        if root1 > root2:
            return (root1, root2)
        else:
            return (root2, root1)