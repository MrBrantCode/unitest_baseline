"""
QUESTION:
Write a function `find_three_elements(arr, target)` that finds three consecutive elements in an array that sum up to a target number. The function takes two parameters: `arr`, an array of integers, and `target`, the target number. Return the three consecutive elements as a list if a solution is found; otherwise, return `None`.
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