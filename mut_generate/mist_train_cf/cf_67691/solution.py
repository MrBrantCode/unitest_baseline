"""
QUESTION:
Construct a Python recursive function named `longest_common_subarray` that takes six parameters: three numerical arrays `X`, `Y`, `Z`, and their corresponding lengths `m`, `n`, `p`. This function should use backtracking principles to find the longest identical sub-array present within the three arrays, where the order of elements matters.
"""

def longest_common_subarray(X, Y, Z, m, n, p):
    if m == 0 or n == 0 or p == 0:
        # Empty arrays have no common subarray
        return []
    
    # If the last elements are the same, it could be part of the longest identical subarray
    if X[m-1] == Y[n-1] == Z[p-1]:
        return longest_common_subarray(X, Y, Z, m-1, n-1, p-1) + [X[m-1]]
    
    # Otherwise, consider the two possibilities: removing the last element of Y and Z, or X and Z, or X and Y
    else:
        xy = longest_common_subarray(X, Y, Z, m-1, n-1, p)
        xz = longest_common_subarray(X, Y, Z, m-1, n, p-1)
        yz = longest_common_subarray(X, Y, Z, m, n-1, p-1)
        
        # Return the longest subarray from the three possibilities
        if len(xy) > len(xz) and len(xy) > len(yz):
            return xy
        elif len(xz) > len(xy) and len(xz) > len(yz):
            return xz
        else:
            return yz