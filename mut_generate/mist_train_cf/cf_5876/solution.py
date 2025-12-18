"""
QUESTION:
Write a function `generateAllPermutations(N)` that generates an array of all possible permutations of N numbers, ranging from 1 to N, with a time complexity of O(N!) and a space complexity of O(N!). The function should return an array of arrays, where each inner array represents a permutation.
"""

def generateAllPermutations(N):
    def generatePermutations(current):
        if len(current) == N:
            result.append(current[:])  # make a copy of current and append to result
            return
        
        for num in range(1, N+1):
            if num not in current:
                current.append(num)
                generatePermutations(current)
                current.pop()  # backtrack
                
    result = []
    generatePermutations([])
    return result