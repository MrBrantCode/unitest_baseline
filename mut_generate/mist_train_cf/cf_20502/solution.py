"""
QUESTION:
Generate a function named `generateAllPermutations` that takes a positive integer `N` as input and returns an array of all possible permutations of numbers from 1 to `N`. The time complexity of the function should be O(N!) and the space complexity should be O(N!).
"""

def generateAllPermutations(N):
    def generatePermutations(current, result):
        if len(current) == N:
            result.append(current.copy())
            return
        
        for i in range(1, N+1):
            if i not in current:
                current.append(i)
                generatePermutations(current, result)
                current.pop()

    result = []
    generatePermutations([], result)
    return result