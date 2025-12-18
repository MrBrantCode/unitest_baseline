"""
QUESTION:
Create a function `remove_duplicates_2D_list` that takes a 2D list as input and returns a new 2D list with all duplicate elements removed, maintaining the original order of elements. The solution should not use any built-in functions or libraries for removing duplicates and should have a time complexity of less than O(m*n^2) and a space complexity of O(m*n), where m is the number of rows and n is the number of columns in the input list.
"""

def remove_duplicates_2D_list(lst):
    # create a set to store unique elements
    seen = set()
    
    # create a new list to store the result
    result = []
    
    # loop through the lists in the given 2D list
    for sublist in lst:
        new_sublist = []
        for element in sublist:
            # if the element has not been encountered before, add it to the set 
            # and the new sublist
            if element not in seen:
                seen.add(element)
                new_sublist.append(element)
        # add the new sublist to the result
        result.append(new_sublist)
    
    return result