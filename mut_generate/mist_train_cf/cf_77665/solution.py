"""
QUESTION:
Write a function `T(r)` to calculate the count of integer quadruplets `x, y, z, t` that satisfy the inequality `x^2 + y^2 + z^2 + t^2 ≤ r^2` modulo `1000000007`, where `r` is a positive integer. Use the approximation `T(r) = c * r^4` to estimate the result, with `c` being the constant of proportionality. The function should take no arguments and return the value of `T(10^8)` modulo `1000000007`.
"""

def T(r):
    # Pre-calculated constants
    T_r = 493490641
    r_calculated = 100

    # Calculate constant c
    c = T_r / (r_calculated**4)

    # Calculate result
    result = int(c*(r**4) % 1000000007)
    
    return result

# Call the function with r = 10^8
print(T(10**8))