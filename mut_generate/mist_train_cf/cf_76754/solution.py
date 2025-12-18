"""
QUESTION:
Write a function `longest_diagonal(cube, target)` that takes a 3D list `cube` and an integer `target` as input. The function should return the longest diagonal in `cube` where the product of its elements equals `target`. A diagonal is defined as a sequence of elements where the indices of each element increase by 1 in all dimensions. The function should assume that `cube` is a perfect cube, i.e., it has equal dimensions along each axis.
"""

def longest_diagonal(cube, target):
    longest_diag = []
    for a in range(len(cube)):
        for b in range(len(cube[a])):
            for c in range(len(cube[a][b])):
                # get the diagonals
                diag = []
                for d in range(len(cube)):
                    if a+d<len(cube) and b+d<len(cube[a]) and c+d<len(cube[a][b]):
                        diag.append(cube[a+d][b+d][c+d])
                
                product = 1
                for e in diag:
                    product *= e
                
                # check if product equals target and if this diagonal is the longest
                if product == target and len(diag) > len(longest_diag):
                    longest_diag = diag
                    
    return longest_diag