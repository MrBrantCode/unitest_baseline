"""
QUESTION:
Design a function `minimum_moves` that takes a list of integers as input and returns the minimum number of moves required to sort the list in ascending order, where a move is defined as swapping two adjacent elements. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def minimum_moves(nums):
    """
    This function calculates the minimum number of moves required to sort a list of integers in ascending order.
    
    A move is defined as swapping two adjacent elements. The function uses a selection sort approach and has a time complexity of O(n^2) and a space complexity of O(1).
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        int: The minimum number of moves required to sort the list.
    """
    
    # Initialize a variable to keep track of the number of moves required.
    moves = 0
    
    # Iterate through the array from index 0 to n-1.
    for i in range(len(nums) - 1):
        
        # Initialize a variable to store the index of the minimum element found so far.
        minIndex = i
        
        # Iterate through the array from index i+1 to n-1 to find the minimum element.
        for j in range(i + 1, len(nums)):
            
            # If the element at index j is smaller than the element at index minIndex, update minIndex.
            if nums[j] < nums[minIndex]:
                minIndex = j
        
        # If minIndex is not equal to i, swap the elements at indices i and minIndex, increment moves by 1.
        if minIndex != i:
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
            moves += 1
    
    # Return the value of moves.
    return moves