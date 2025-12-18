"""
QUESTION:
Implement a function named `solve_equation(n)` to find all integer solutions for the equation x^4 + y^4 = z^4 where x, y, and z are integers between 1 and n (inclusive). The function should return a list of tuples, where each tuple contains a solution (x, y, z).
"""

def solve_equation(n):
    solutions = []
    
    for x in range(1, n+1):
        for y in range(1, n+1):
            z = (x**4 + y**4) ** 0.25  # Calculate z using the fourth root
            if z.is_integer() and z <= n:  # Check if z is an integer and within the given range
                solutions.append((x, y, int(z)))
    
    return solutions