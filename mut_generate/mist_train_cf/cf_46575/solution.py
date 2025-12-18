"""
QUESTION:
Create a function `combinationSum` that takes two parameters: a list of integers `candidates` and a target integer `target`. The function should return all unique combinations of integers from the `candidates` list that sum up to the `target` value. Note that each integer in the `candidates` list can be used multiple times, and the order of the integers in the combinations does not matter.
"""

def combinationSum(candidates, target):
    def findNumbers(candidates, target, currentSum, start, output, combination):
        if currentSum > target: 
            return
        if currentSum == target: 
            output.append(list(combination))
            return
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            findNumbers(candidates, target, currentSum+candidates[i], i, output, combination)  
            combination.pop()  

    output = []
    findNumbers(candidates, target, 0, 0, output, [])
    return output