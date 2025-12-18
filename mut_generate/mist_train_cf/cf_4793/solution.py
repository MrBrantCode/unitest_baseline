"""
QUESTION:
Create a function `find_pair(numbers, target)` that takes an array of integers `numbers` and an integer `target` as input. The function should return a pair of elements in the array whose sum matches the target. If multiple pairs exist, return the pair with the highest sum. If no such pair exists, return an empty array. If there are multiple pairs with the highest sum, return the pair with the smallest first element. The length of the array `numbers` will not exceed 10^9 and the elements in the array will be integers between -10^18 and 10^18. The target will be an integer between -10^18 and 10^18.
"""

def find_pair(numbers, target):
    pairs = []
    max_sum = float('-inf')
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                current_sum = numbers[i] + numbers[j]
                if current_sum > max_sum:
                    max_sum = current_sum
                    pairs = [numbers[i], numbers[j]]
                elif current_sum == max_sum and numbers[i] < pairs[0]:
                    pairs = [numbers[i], numbers[j]]
    
    return pairs