"""
QUESTION:
Mikhail the Freelancer dreams of two things: to become a cool programmer and to buy a flat in Moscow. To become a cool programmer, he needs at least p experience points, and a desired flat in Moscow costs q dollars. Mikhail is determined to follow his dreams and registered at a freelance site.

He has suggestions to work on n distinct projects. Mikhail has already evaluated that the participation in the i-th project will increase his experience by a_{i} per day and bring b_{i} dollars per day. As freelance work implies flexible working hours, Mikhail is free to stop working on one project at any time and start working on another project. Doing so, he receives the respective share of experience and money. Mikhail is only trying to become a cool programmer, so he is able to work only on one project at any moment of time.

Find the real value, equal to the minimum number of days Mikhail needs to make his dream come true.

For example, suppose Mikhail is suggested to work on three projects and a_1 = 6, b_1 = 2, a_2 = 1, b_2 = 3, a_3 = 2, b_3 = 6. Also, p = 20 and q = 20. In order to achieve his aims Mikhail has to work for 2.5 days on both first and third projects. Indeed, a_1·2.5 + a_2·0 + a_3·2.5 = 6·2.5 + 1·0 + 2·2.5 = 20 and b_1·2.5 + b_2·0 + b_3·2.5 = 2·2.5 + 3·0 + 6·2.5 = 20.


-----Input-----

The first line of the input contains three integers n, p and q (1 ≤ n ≤ 100 000, 1 ≤ p, q ≤ 1 000 000) — the number of projects and the required number of experience and money.

Each of the next n lines contains two integers a_{i} and b_{i} (1 ≤ a_{i}, b_{i} ≤ 1 000 000) — the daily increase in experience and daily income for working on the i-th project.


-----Output-----

Print a real value — the minimum number of days Mikhail needs to get the required amount of experience and money. Your answer will be considered correct if its absolute or relative error does not exceed 10^{ - 6}. 

Namely: let's assume that your answer is a, and the answer of the jury is b. The checker program will consider your answer correct, if $\frac{|a - b|}{\operatorname{max}(1, b)} \leq 10^{-6}$.


-----Examples-----
Input
3 20 20
6 2
1 3
2 6

Output
5.000000000000000

Input
4 1 1
2 3
3 2
2 3
3 2

Output
0.400000000000000



-----Note-----

First sample corresponds to the example in the problem statement.
"""

def calculate_minimum_days(n, p, q, ABs):
    """
    Calculate the minimum number of days Mikhail needs to achieve his dream of 
    gaining at least p experience points and earning at least q dollars.

    Parameters:
    n (int): The number of projects.
    p (int): The required experience points.
    q (int): The required amount of money.
    ABs (list of tuples): A list of tuples where each tuple contains the daily 
                          experience gain (a_i) and daily income (b_i) for each project.

    Returns:
    float: The minimum number of days required to achieve the goals.
    """
    
    def get_bounds(points):
        if len(points) == 1:
            return points[:]
        points.sort()
        bounds = [points[0], points[1]]
        for (xi, yi) in points[2:]:
            while len(bounds) > 1 and (not is_convex(bounds, xi, yi)):
                del bounds[-1]
            bounds.append((xi, yi))
        return bounds

    def is_convex(bounds, x2, y2):
        (x1, y1) = bounds[-1]
        (x0, y0) = bounds[-2]
        return (x1 - x0) * (y2 - y1) < (y1 - y0) * (x2 - x1)

    bounds = get_bounds(ABs)
    (a0, b0) = bounds[0]
    if len(bounds) == 1:
        return max(p / a0, q / b0)
    record = float('Inf')
    for (a1, b1) in bounds[1:]:
        steps = min(max(p / a0, q / b0), max(p / a1, q / b1))
        den = a0 * b1 - b0 * a1
        if den != 0:
            r0 = (b1 * p - a1 * q) / den
            r1 = -(b0 * p - a0 * q) / den
            if r0 > 0 and r1 > 0:
                steps = min(steps, r0 + r1)
        a0 = a1
        b0 = b1
        record = min(record, steps)
    return record