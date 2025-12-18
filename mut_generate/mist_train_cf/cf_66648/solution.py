"""
QUESTION:
Write a function `five_div_seq(n)` that takes an integer `n` as input and returns the number of times the digit 5 appears in integers below `n` that are divisible by either 9 or 14. The integers must be at least 3 digits long and form a descending arithmetic sequence with an even constant difference.
"""

def five_div_seq(n: int) -> int:
    # Initialize our counter to 0
    five_count = 0

    # Loop from n down to 1
    for i in range(n, 0, -1):
        # Check if i is divisible by either 9 or 14
        if i % 9 == 0 or i % 14 == 0:
            # Convert i to a string
            str_i = str(i)
            # Check if the integer is at least 3 digits long
            if len(str_i) >= 3:
                # Count the number of times 5 appears in the string
                five_count += str_i.count('5')

    return five_count