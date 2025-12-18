"""
QUESTION:
Write a function harmonic_progression_cumulative(M, N) that takes two integers M and N as input where M < N. The function should calculate the cumulative total of the harmonic progression beginning at 1/M and incrementally increasing by 1 with each subsequent term, ending at 1/N. The function should handle irregular patterns and missing numbers in the sequence, and provide a return message that signifies whether the error is caused by invalid inputs or an arithmetic error. Do not use any pre-built function or library for harmonic series.
"""

def harmonic_progression_cumulative(M, N):
    # Check that M and N are integers and that M < N
    if not (isinstance(M, int) and isinstance(N, int)):
        return "Invalid input: Inputs must be integers."
    elif M >= N:
        return "Invalid input: M must be less than N."

    try:
        # Initialize the cumulative total
        cumulative_total = 0
        # Cycle through the harmonic sequence, skipping missing items
        for i in range(M, N+1):
            # Skip irregular patterns or missing numbers in the sequence
            if i == 0 or i is None:
                continue
            cumulative_total += 1/i
    except Exception as e:
        return "An arithmetic error occurred: " + str(e)

    return cumulative_total