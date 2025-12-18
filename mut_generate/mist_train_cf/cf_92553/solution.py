"""
QUESTION:
Write a function `generateAllPermutations` that generates an array of all possible permutations of N numbers, where N is a positive integer. The numbers in the array can range from 1 to N. The function should take an integer N as input and return a 2D array of all possible permutations.

The function should follow these restrictions:
- The input N is a positive integer.
- The numbers in the permutations can range from 1 to N.
- The function should return all unique permutations of the numbers from 1 to N.
- The function should return a 2D array, where each sub-array is a permutation of the numbers from 1 to N.
"""

def generateAllPermutations(N):
    result = []
    def generatePermutations(current):
        if len(current) == N:
            result.append(list(current))
            return
        for i in range(1, N+1):
            if i not in current:
                current.append(i)
                generatePermutations(current)
                current.pop()
    generatePermutations([])
    return result