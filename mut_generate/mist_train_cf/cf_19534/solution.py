"""
QUESTION:
Create a function `find_pair_with_highest_sum` that takes two parameters: `numbers`, an array of integers, and `target`, an integer. The function should find a pair of elements in `numbers` whose sum matches `target`. If multiple pairs exist, return the pair with the highest sum. If no such pair exists, return an empty array. If there are multiple pairs with the highest sum, return the pair with the smallest first element. 

The length of `numbers` will not exceed 10^6, the elements in `numbers` will be integers between -10^12 and 10^12, and the target will be an integer between -10^12 and 10^12.
"""

def find_pair_with_highest_sum(numbers, target):
    # Sort the array in ascending order
    numbers.sort()
    
    # Initialize two pointers
    left = 0
    right = len(numbers) - 1
    
    # Initialize variables to track the highest sum and the pair with the highest sum
    highest_sum = float('-inf')
    highest_sum_pair = []
    
    # Loop until the two pointers cross each other
    while left < right:
        # Calculate the sum of the current pair
        current_sum = numbers[left] + numbers[right]
        
        # If the current sum matches the target, we have found a pair
        if current_sum == target:
            return [numbers[right], numbers[left]]
        
        # If the current sum is greater than the target and it is the highest sum so far, update the highest sum and the pair
        if current_sum > target and current_sum > highest_sum:
            highest_sum = current_sum
            highest_sum_pair = [numbers[right], numbers[left]]
        
        # Move the pointers based on the current sum
        if current_sum < target:
            left += 1
        else:
            right -= 1
    
    # If no pair with the highest sum is found, return an empty array
    return highest_sum_pair