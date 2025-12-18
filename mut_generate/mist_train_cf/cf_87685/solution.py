"""
QUESTION:
Create a function named `print_array` that takes a 2D array `arr` as input. The function should print all elements of the 2D array in row-wise order, with each element printed exactly once, without using any loops or recursion, and with a time complexity of O(n) and space complexity of O(n), where n is the total number of elements in the array.
"""

def print_array(arr):
    # Create a set to keep track of printed elements
    printed = set()
    
    # Define a helper function to print the elements
    def print_helper(row, col):
        # Check if the element has already been printed
        if (row, col) in printed or row >= len(arr) or col >= len(arr[0]):
            return
        
        # Print the current element
        print(arr[row][col])
        
        # Add the element to the set of printed elements
        printed.add((row, col))
        
        # Calculate the next row and column indices
        next_row = row
        next_col = (col + 1) % len(arr[row])
        if next_col == 0:
            next_row = (row + 1) % len(arr)
        
        # Call the helper function recursively
        print_helper(next_row, next_col)
    
    # Start the recursive function at the first element
    print_helper(0, 0)