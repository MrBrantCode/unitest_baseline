"""
QUESTION:
Example

Input

2 2 2 1
0 0 0


Output

24
"""

def calculate_surface_area(a, b, c, n, aa):
    # Calculate the initial surface area of the cuboid
    r = (a * b + b * c + c * a) * 2
    
    # Adjust the surface area for each additional cube
    for (d, e, f) in aa:
        r += 6
        if d == 0:
            r -= 2
        if e == 0:
            r -= 2
        if f == 0:
            r -= 2
        if d == a - 1:
            r -= 2
        if e == b - 1:
            r -= 2
        if f == c - 1:
            r -= 2
    
    # Function to calculate the Manhattan distance between two points
    def manhattan_distance(a, b):
        return sum(abs(a[i] - b[i]) for i in range(3))
    
    # Adjust the surface area for adjacent cubes
    for i in range(n):
        ai = aa[i]
        for j in range(i + 1, n):
            if manhattan_distance(ai, aa[j]) == 1:
                r -= 2
    
    return r