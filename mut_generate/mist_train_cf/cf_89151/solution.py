"""
QUESTION:
Write a function `generateAllPermutations` that takes a positive integer `N` as input and generates an array of all possible permutations of `N` numbers. The numbers in the array should range from 1 to `N`. The function should have a time complexity of `O(N!)` and a space complexity of `O(N!)`.
"""

def generateAllPermutations(N):
    result = []
    
    def generatePermutations(current):
        if len(current) == N:
            result.append(current[:])  # make a copy of current and append to result
            return
        
        for num in range(1, N+1):
            if num not in current:
                current.append(num)
                generatePermutations(current)
                current.pop()  # backtrack
                
    generatePermutations([])
    return result