"""
QUESTION:
Function: binary_gap(n)
Information: This function takes a positive integer n and returns the greatest distance between any two consecutive 1's in the binary representation of n. If no such pair of 1's exists, the function returns 0. Consecutive 1's are defined as 1's separated solely by 0's or not separated at all. The distance between two 1's is the absolute difference in their bit positions.
Restrictions: 1 <= n <= 10^9.
"""

def binaryGap(n):
    binary = bin(n)[2:]  # Converts the integer to binary and removes the '0b' prefix
    index_of_last_one = -1  # Keep track of the index of the last '1' bit
    max_gap = 0  # Initialize the maximum binary gap

    # Loop over each bit in the binary representation from left to right
    for i in range(len(binary)):
        if binary[i] == '1':  # If the current bit is '1'
            if index_of_last_one >= 0:  # If there was a '1' bit before this
                # Get the distance between the current '1' bit and the last '1' bit
                gap = i - index_of_last_one
                # Update the max_gap if the current gap is greater
                max_gap = max(max_gap, gap)
            index_of_last_one = i  # Update the index of the last '1' bit

    return max_gap