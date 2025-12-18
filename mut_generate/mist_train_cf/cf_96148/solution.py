"""
QUESTION:
Write a function `generateAllPermutations(N)` to generate an array of all possible permutations of N numbers, where N is a positive integer. The numbers in the array can range from 1 to N. The function should have a time complexity of O(N!) and a space complexity of O(N!).
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