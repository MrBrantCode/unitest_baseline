"""
QUESTION:
Write a function named `print_array` that prints all elements in a given 2D array in row-wise order. The function should not use any loops or recursion. Each element of the array is a positive integer less than or equal to 100.
"""

def print_array(arr):
    # Create a set to keep track of printed elements
    printed = set()
    
    # Define a helper function to print the elements
    def print_helper(row, col):
        # Check if the element has already been printed
        if (row, col) in printed or row >= len(arr) or col >= len(arr[row]):
            if row == 0 and col == 0:
                return
            next_row = row
            next_col = (col + 1) % len(arr[row])
            if next_col == 0:
                next_row = (row + 1) % len(arr)
            print_helper(next_row, next_col)
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