"""
QUESTION:
Write a function called `findIntegers` that takes a positive integer `n` as input and returns the number of non-negative integers less than or equal to `n` whose binary representations do not contain consecutive zeros. The input integer `n` is in the range 1 <= n < 10^9.
"""

def findIntegers(n):
    binary = bin(n)[2:]

    endsInZero, endsInOne = [0] * len(binary), [0] * len(binary)
    endsInZero[0], endsInOne[0] = 1, 1

    for i in range(1, len(binary)):
        endsInZero[i] = endsInZero[i - 1] + endsInOne[i - 1]      
        endsInOne[i] = endsInZero[i - 1]                           

    result = endsInZero[-1] + endsInOne[-1]

    for i in range(len(binary) - 2, -1, -1):
        if binary[i:i + 2] == '11':
            break
        if binary[i:i + 2] == '00':
            result -= endsInOne[i]
    
    return result - 1   # subtract 1 to exclude the number itself