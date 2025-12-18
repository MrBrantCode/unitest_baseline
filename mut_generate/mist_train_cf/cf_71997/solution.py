"""
QUESTION:
Create a recursive function `pascal(height)` that generates Pascal's Triangle given the height as an input. The function should consider the mathematical properties of Pascal's Triangle, where each number is the sum of the two numbers directly above it. The function should return a 2D list representing the triangle, where each inner list represents a row in the triangle. The height of the triangle should be at least 1.
"""

def pascal(height):
    if height == 1:
       return [[1]]
    else:
       triangle = pascal(height - 1)
       last_row = triangle[-1]
       new_row = [1]
       for i in range(len(last_row) - 1):
           new_row.append(last_row[i] + last_row[i + 1])
       new_row.append(1)
       triangle.append(new_row)
    return triangle