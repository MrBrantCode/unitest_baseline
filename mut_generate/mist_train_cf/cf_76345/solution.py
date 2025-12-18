"""
QUESTION:
Implement a function `maxOnes(width, height, sideLength, maxOnes)` that calculates the maximum possible number of ones in a matrix `M` of dimensions `width * height`, where each cell can contain a value of `0` or `1` and any square sub-matrix of size `sideLength * sideLength` can contain at most `maxOnes` ones. 

Constraints: `1 <= width, height <= 100`, `1 <= sideLength <= width, height`, `0 <= maxOnes <= sideLength * sideLength`.
"""

def maxOnes(width, height, sideLength, maxOnes):
    total = width * height  
    q, r = divmod(total, (sideLength * sideLength))  
    onecells = min(maxOnes, r) 
    return q * maxOnes + onecells