"""
QUESTION:
Implement a function `solve_equation(n)` that finds all integer solutions to the equation x^4+y^4=z^4 where x, y, and z are integers between 1 and n. The function should return a list of tuples containing all unique solutions (x, y, z).
"""

def solve_equation(n):
    solutions = []
    
    for x in range(1, n+1):
        for y in range(x, n+1):  # Optimized loop to avoid duplicates
            z = (x**4 + y**4) ** 0.25  # Calculate z using the fourth root
            if z.is_integer() and z <= n:  # Check if z is an integer and within the given range
                solutions.append((x, y, int(z)))
    
    return solutions