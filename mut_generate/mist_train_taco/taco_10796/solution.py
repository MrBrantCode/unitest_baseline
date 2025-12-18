"""
QUESTION:
Example

Input

4 3
1000 1
2000 2
3000 3


Output

2 3 4 4
"""

def calculate_ranges(N, M, XY):
    # Sort the input list of tuples by the first element of each tuple
    XY.sort(key=lambda x: x[0])
    
    # Initialize minY and maxY lists
    minY = list(range(N))
    maxY = list(range(N))
    
    # Process each pair (x, y) in XY
    for _, y in XY:
        y0, y1 = y - 1, y
        minY[y1] = minY[y0]
        maxY[y0] = maxY[y1]
    
    # Calculate the answer list
    ans = [maxY[i] - minY[i] + 1 for i in range(N)]
    
    return ans