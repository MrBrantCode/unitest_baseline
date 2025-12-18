"""
QUESTION:
problem

Given $ N $ different natural numbers $ a_i $. I decided to make a pair by choosing a different natural number from the given natural numbers. Output one pair that can be created with a value difference that is a multiple of $ N -1 $.

It should be noted that such a pair always exists.





Example

Input

5
1 2 4 7 10


Output

2 10
"""

def find_pair_with_difference_multiple(N, a):
    for i in range(N):
        for j in range(N):
            if i != j and abs(a[i] - a[j]) % (N - 1) == 0:
                return (a[i], a[j])
    return None  # This line should never be reached because such a pair always exists