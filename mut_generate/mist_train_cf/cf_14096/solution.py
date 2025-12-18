"""
QUESTION:
Create a function named `find_largest_common_factor` that takes three parameters: `N1`, `N2`, and `R`. The function should find the largest common factor of `N1` and `N2` within the range of 1 to `R`. If no common factor exists within this range, the function should return -1.
"""

def find_largest_common_factor(N1, N2, R):
    # Find the smaller number between N1 and N2
    if N1 < N2:
        smaller = N1
    else:
        smaller = N2
    
    largest_common_factor = -1
    # Iterate from 1 to R
    for i in range(1, R + 1):
        # Check if i is a factor of both N1 and N2
        if N1 % i == 0 and N2 % i == 0:
            # Update the largest common factor
            largest_common_factor = i
    
    return largest_common_factor