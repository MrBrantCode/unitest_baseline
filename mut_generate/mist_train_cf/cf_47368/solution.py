"""
QUESTION:
Write a function `find_isolated_ones(num)` that takes an integer `num` as input and returns an array of indices (counting from right-to-left, starting at 0) of the binary representation of `num` where there are isolated ones, i.e., '1' bits with no adjacent '1' bits on either side.
"""

def find_isolated_ones(num):
    # Convert the number to binary and remove the first two characters of the output of bin function
    binNum = bin(num)[2:]
    isolated_ones_indices = []

    # Reverse the string because we are counting from right to left
    reversedBinNum = binNum[::-1]

    for i in range(len(reversedBinNum)):
        # Ignore first and last bit
        if i == 0 or i == len(reversedBinNum) - 1:
            continue

        # Checking if bit is '1' and it's adjacent bits are '0'
        if reversedBinNum[i] == '1' and reversedBinNum[i-1] == '0' and reversedBinNum[i+1] == '0':
            isolated_ones_indices.append(i)

    return isolated_ones_indices