"""
QUESTION:
Create a function `generate_pascals_triangle(row_num)` that generates Pascal's triangle up to the given row number. The function should only generate the triangle if the row number is a prime number; otherwise, it should return without generating the triangle.
"""

def generate_pascals_triangle(row_num):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    if not is_prime(row_num):
        print("Row number should be a prime number.")
        return
    
    triangle = []
    
    for i in range(row_num):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    
    return triangle