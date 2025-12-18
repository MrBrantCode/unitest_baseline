"""
QUESTION:
Write a function `compute_min_N(N)` that finds the least value of N such that the number of rectangular prisms with integer dimensions, up to a maximum size of N by N by N, for which the shortest route has integer length exceeds two million. The function should return the minimum value of N. 

The shortest route for a rectangular prism with sides a, b, c is equal to the length of the shortest geodesic on the cuboid, which is the smallest of √(a² + (b+c)²), √(b² + (a+c)²), √(c² + (a+b)²). The function should count the number of integer solutions (a, b, c) for each possible length x, where a ≤ b ≤ c < x and a² + (b+c)² = x².
"""

def compute_min_N(N):
    total = 0
    sides = [0] * (N + 1)
    for z in range(1, N + 1, 2):
        z_sq = z ** 2
        for x in range(2, N + 1, 2):
            x_sq = x ** 2
            if 4 * x_sq <= z_sq:
                t_max = int((z_sq - x_sq) ** 0.5)
                t_min = (-(-x // 2)) + ((x & z & 1) ^ 1)
                sides[z] += (t_max - t_min) // 2 + 1
            else:
                break
        total += sides[z]
        if total > 2000000:
            return z