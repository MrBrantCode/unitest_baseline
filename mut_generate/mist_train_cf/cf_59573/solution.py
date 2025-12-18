"""
QUESTION:
Implement a function `monotonic_advanced` that takes a list `l`, a boolean `strict`, another boolean `zero_crossing`, and a string `progression` as parameters. The function should return `True` if the elements of the list increase or decrease monotonically, considering the following conditions:

- If `progression` is "arithmetic", the list should form an arithmetic progression.
- If `progression` is "geometric", the list should form a geometric progression.
- If `strict` is `True`, no two consecutive elements in the list can be identical.
- If `zero_crossing` is `True`, the list can change from increasing to decreasing or vice versa only at a zero element.
"""

def monotonic_advanced(l: list, strict: bool = False, zero_crossing: bool = False, progression: str = None):
    # Edge case for empty list or single element list
    if len(l) < 2:
        return True

    if progression == "arithmetic":
        # Check for arithmetic progression
        diff = l[1] - l[0]
        for i in range(2, len(l)):
            if l[i] - l[i-1] != diff:
                return False
    elif progression == "geometric":
        # Check for geometric progression (avoiding division by zero)
        if l[0] != 0:
            ratio = l[1] / l[0]
            for i in range(2, len(l)):
                if l[i-1] != 0 and l[i] / l[i-1] != ratio:
                    return False
        else:
            return False

    # Check for strict monotonicity
    if strict:
        for i in range(1, len(l)):
            if l[i] == l[i-1]:
                return False

    # Check for mono-tonicity with zero_crossing
    if zero_crossing:
        crossing = False
        for i in range(1, len(l)):
            if l[i] * l[i-1] < 0:
                if crossing:
                    return False
                crossing = True

    # Check for general monotonicity
    increase = False
    decrease = False
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            increase = True
        elif l[i] < l[i-1]:
            decrease = True
        if increase and decrease:
            return False

    return True