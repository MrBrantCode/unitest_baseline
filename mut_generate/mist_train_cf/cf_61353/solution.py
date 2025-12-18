"""
QUESTION:
Develop an algorithm that merges two descending-ordered lists of floating-point numbers, X and Y, into a single list in descending order. Implement a function merge_descending(X, Y) that takes in these two lists and returns the merged list.
"""

def merge_descending(X, Y):
    i = j = 0
    merged_list = []
    
    # Run while there are elements left in both lists
    while i < len(X) and j < len(Y):
        if X[i] > Y[j]:
            merged_list.append(X[i])
            i += 1
        else:
            merged_list.append(Y[j])
            j += 1

    # If there are remaining elements in X, append them to the merged list
    while i < len(X):
        merged_list.append(X[i])
        i += 1

    # If there are remaining elements in Y, append them to the merged list
    while j < len(Y):
        merged_list.append(Y[j])
        j += 1
   
    return merged_list