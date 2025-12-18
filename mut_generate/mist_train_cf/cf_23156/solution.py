"""
QUESTION:
Write a function `find_three_elements(arr, target)` that takes an array of integers `arr` and a target number `target` as input, and returns three consecutive elements in the array that sum up to the target number. If no such elements exist, return `None`.
"""

def find_three_elements(arr, target):
    n = len(arr)
    
    for start in range(n-2):
        middle = start + 1
        end = start + 2
        
        while end < n:
            current_sum = arr[start] + arr[middle] + arr[end]
            
            if current_sum == target:
                return [arr[start], arr[middle], arr[end]]
            
            if current_sum < target:
                end += 1
            else:
                start += 1
                middle += 1
                
    return None