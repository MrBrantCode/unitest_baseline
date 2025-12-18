"""
QUESTION:
problem

A mysterious $ X $ [cm] plant grows in one place. This plant has the following mysterious properties.

* Say "nobiro" to this plant and it will grow $ A $ [cm].
* Say "tidime" to this plant and it will grow $ B $ [cm].
* If you say "karero" to this plant, it will be $ 0 $ [cm].



However, this plant does not have a negative length. Specifically, when it grows from the state of $ C $ [cm] to $ D $ [cm] $ (C + D \ lt 0) $, it is a plant. Stops growing when it reaches $ 0 $ [cm].

Say one of "nobiro", "tidime", "karero" to this plant only once a day for $ N $ days. Find the length [cm] of the plant after $ N $ days.



output

Print the length of the plant after $ N $ days. Also print a newline at the end.

Example

Input

10 30 10
3
nobiro
nobiro
tidime


Output

80
"""

def calculate_plant_length(X, A, B, N, S):
    for s in S:
        if s == 'nobiro':
            X += A
        elif s == 'tidime':
            X += B
        else:
            X = 0
        if X < 0:
            X = 0
    return X