"""
QUESTION:
The function `racecar` should take an integer `target` as input, where `1 <= target <= 10000`, and return the minimum number of instructions needed to reach the target position on an infinite number line. The car starts at position 0 with speed +1 and can move according to instructions A (accelerate), R (reverse), and B (brake), which change the car's position and speed as follows: 
- A: `position += speed, speed *= 2`
- R: if `speed` is positive then `speed = -1`, otherwise `speed = 1`
- B: `speed = speed / 2` (rounded down to the nearest integer).
"""

def racecar(target):
    A = [0, 1, 4] + [float('inf')] * target
    for t in range(3, target + 1):
        b = t.bit_length()
        if t == 2**b - 1:
            A[t] = b
            continue
        for j in range(b - 1):
            A[t] = min(A[t], A[t - 2**(b - 1) + 2**j] + b - 1 + j + 2)
        if 2**b - 1 - t < t:
            A[t] = min(A[t], A[2**b - 1 - t] + b + 1)
    return A[target]