"""
QUESTION:
Write a function `find_largest_common_factor(N1, N2, R)` that takes two numbers `N1` and `N2`, and a range `R`, and returns the largest common factor of `N1` and `N2` that is within the range of 1 to `R`. If there is no common factor within the range, the function should return -1.
"""

def find_largest_common_factor(N1, N2, R):
    # Find the smaller number between N1 and N2
    if N1 < N2:
        smaller = N1
    else:
        smaller = N2
    
    largest_common_factor = -1
    # Iterate from R to 1
    for i in range(R, 0, -1):
        # Check if i is a factor of both N1 and N2
        if N1 % i == 0 and N2 % i == 0:
            # Update the largest common factor
            largest_common_factor = i
            break
    
    return largest_common_factor