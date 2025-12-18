"""
QUESTION:
Construct a function named `shell_sort` that sorts a given list of integers in ascending order using the shell sort algorithm. The function should sort the list in-place, meaning it modifies the original list instead of creating a new sorted copy. The function should not take any additional parameters other than the list to be sorted.
"""

def entance(collection):
    # Determine the initial gap (half the size of the collection, rounded down)
    gap = len(collection) // 2
    
    # While the gap is greater than zero...
    while gap > 0:       
        # For every index in the range between the gap and the end of the collection...
        for i in range(gap, len(collection)):            
            temp = collection[i]  # temp variable to hold the current item
            j = i  # set j to the current index
            
            # While j is greater than or equal to the gap and the item at index j-gap is greater than the temp value...
            while j >= gap and collection[j - gap] > temp:  
                # Swap the places of the two items
                collection[j] = collection[j - gap]
                j -= gap  # decrement j by the gap
                
            collection[j] = temp  # set the item at index j to the temp value
        
        gap //= 2  # halve the gap
    
    return collection  # return the sorted collection