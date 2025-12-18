"""
QUESTION:
The Zoo in the Grid Kingdom is represented by an infinite grid. The Zoo has n observation binoculars located at the OX axis. For each i between 1 and n, inclusive, there exists a single binocular located at the point with coordinates (i, 0). There are m flamingos in the Zoo, located at points with positive coordinates. The flamingos are currently sleeping and you can assume that they don't move.

In order to get a good view over the flamingos, each of the binoculars can be independently rotated to face any angle (not necessarily integer). Then, the binocular can be used to observe all flamingos that is located at the straight line passing through the binocular at the angle it is set. In other words, you can assign each binocular a direction corresponding to any straight line passing through the binocular, and the binocular will be able to see all flamingos located on that line.

Today, some kids from the prestigious Codeforces kindergarten went on a Field Study to the Zoo. Their teacher would like to set each binocular an angle to maximize the number of flamingos that can be seen by the binocular. The teacher is very interested in the sum of these values over all binoculars. Please help him find this sum.

Input

The first line contains two space-separated integers n and m (1 ≤ n ≤ 106, 1 ≤ m ≤ 250), denoting the number of binoculars and the number of flamingos, respectively.

Then m lines follow, the i-th line will contain two space-separated integers xi and yi (1 ≤ xi, yi ≤ 109), which means that the i-th flamingo is located at point (xi, yi). 

All flamingos will be located at distinct points.

Output

Print a single integer denoting the maximum total number of flamingos that can be seen by all the binoculars.

Examples

Input

5 5
2 1
4 1
3 2
4 3
4 4


Output

11

Note

This picture shows the answer to the example test case. 

<image>
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def normalize_rational(num, den):
    if num ^ den < 0 and num > 0 or (num ^ den > 0 and num < 0):
        num = -num
        den = -den
    g = gcd(abs(num), abs(den))
    num //= g
    den //= g
    return (num, den)

def calculate_max_flamingos_seen(n, m, flamingos):
    maxhits = [1] * (n + 1)
    maxhits[0] = 0
    
    xs = [flamingo[0] for flamingo in flamingos]
    ys = [flamingo[1] for flamingo in flamingos]
    
    line_to_points = {}
    
    for i in range(m):
        for j in range(m):
            dy = ys[i] - ys[j]
            dx = xs[i] - xs[j]
            if dy == 0:
                continue
            else:
                slope = normalize_rational(dy, dx)
                c_prime = ys[i] * dx - xs[i] * dy
                x_intercept = -c_prime / dy
                line = (slope, x_intercept)
                if line in line_to_points:
                    points = line_to_points[line]
                    points.add(i)
                    points.add(j)
                    continue
                if int(x_intercept) == x_intercept and x_intercept <= n and (x_intercept > 0):
                    points = set([i, j])
                    line_to_points[line] = points
    
    for (line, points) in line_to_points.items():
        x_intercept = int(line[1])
        maxhits[x_intercept] = max(maxhits[x_intercept], len(points))
    
    return sum(maxhits)