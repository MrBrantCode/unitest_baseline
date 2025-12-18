"""
QUESTION:
Generate a function named `generateAllPermutations` that takes a positive integer N as input and returns an array of all possible permutations of numbers from 1 to N.
"""

def generateAllPermutations(N):
    def generatePermutations(current):
        # Base case: if current has N elements, yield it
        if len(current) == N:
            yield current[:]

        # Recursive case: try adding each number from 1 to N
        for i in range(1, N+1):
            if i not in current:
                current.append(i)
                yield from generatePermutations(current)
                current.pop()

    return list(generatePermutations([]))