"""
QUESTION:
Write a function `combinations(arr, length)` and a function `permutations(arr, length)` to generate all possible combinations and permutations of a given array `arr` with a specified `length`. The functions should not use any built-in combination or permutation functions. The generated combinations and permutations should be sorted in descending order based on their sums, and their sums should be printed alongside them. The solution should be optimized to handle arrays with lengths up to 10.
"""

def combinations(arr, length):
    def combination_helper(arr, current, length, result):
        if length == 0:
            result.append(current)
            return
        for i in range(len(arr)):
            combination_helper(arr[i+1:], current + [arr[i]], length - 1, result)
    result = []
    combination_helper(arr, [], length, result)
    result.sort(key=sum, reverse=True)
    for combination in result:
        print(combination, sum(combination))

def permutations(arr, length):
    def permutation_helper(arr, current, length, result):
        if length == 0:
            result.append(current)
            return
        for i in range(len(arr)):
            permutation_helper(arr[:i] + arr[i+1:], current + [arr[i]], length - 1, result)
    result = []
    permutation_helper(arr, [], length, result)
    result.sort(key=sum, reverse=True)
    for permutation in result:
        print(permutation, sum(permutation))