"""
QUESTION:
>When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process  --myjinxin2015 said

# Description:
 Give you two number `m` and `n`(two positive integer, m < n), make a triangle pattern with number sequence `m to n`. The order is clockwise, starting from the top corner, like this:
 
```
 When m=1 n=10  triangle is:
    1
   9 2
  8 0 3
 7 6 5 4
```
 Note: The pattern only uses the last digit of each number; Each row separated by "\n"; Each digit separated by a space; Left side may need pad some spaces, but don't pad the right side; If `m to n` can not make the triangle, return `""`.
  
# Some examples:

```
makeTriangle(1,3) should return:
 1
3 2

makeTriangle(6,20) should return: 

    6
   7 7
  6 8 8
 5 0 9 9
4 3 2 1 0

makeTriangle(1,12) should return ""
 
```
"""

def generate_number_triangle(m, n):
    # Calculate the number of lines and the sum of the first 'lns' natural numbers
    lns, sm = 0, 0
    while sm < n - m + 1:
        lns += 1
        sm += lns
    
    # If the sum exceeds the number of elements, return an empty string
    if sm > n - m + 1:
        return ''
    
    # Initialize the matrix with zeros
    matrix = [[0] * (i + 1) for i in range(lns)]
    
    # Initialize starting position and direction
    y, x, s = 0, 0, 0
    ds = ((1, 1), (0, -1), (-1, 0))
    dy, dx = ds[s]
    
    # Fill the matrix with the sequence
    for i in range(m, n + 1):
        matrix[y][x] = str(i % 10)
        if not 0 <= y + dy < len(matrix) or not 0 <= x + dx < len(matrix[y + dy]) or matrix[y + dy][x + dx]:
            s += 1
            dy, dx = ds[s % 3]
        y, x = y + dy, x + dx
    
    # Format the matrix into the desired output string
    return '\n'.join((' '.join(ln).center(len(matrix[-1]) * 2 - 1).rstrip() for ln in matrix))