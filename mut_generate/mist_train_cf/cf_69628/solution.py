"""
QUESTION:
Develop a function called `five_nine_twelve` that takes an integer `n` as input and returns the count of integers less than `n` that are divisible by either 9 or 12 and contain the digit 5. The function should handle negative input values by immediately returning 0.
"""

def five_nine_twelve(n: int) -> int:
    # If n is negative, immediately return 0.
    # No positive integer can fulfill the conditions if n is negative.
    if n < 0:
        return 0
    
    # Initialize a counter to track the number of valid integers.
    counter = 0
    
    # Iterate over the integers from 5 (the smallest number that can contain the digit 5)
    # up to n - 1 (since n itself is excluded).
    for i in range(5, n):
        # Change the integer to string to check if it contains the digit 5.
        if '5' in str(i):
            # Check for divisibility by 9 or 12.
            if i % 9 == 0 or i % 12 == 0:
                # If all the conditions are met, increment the counter.
                counter += 1
    
    # Finally, return the counter.
    return counter