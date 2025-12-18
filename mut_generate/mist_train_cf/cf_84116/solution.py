"""
QUESTION:
Write a function `find_vect(lst3d, x, y)` that takes a 3D list `lst3d` and two integers `x` and `y` as input. The function should search for occurrences of `x` and `y` at consecutive indices in the 3D list and return a list of tuples, where each tuple contains the depth, row, and index of the occurrence. The tuples in the output list should be in ascending order based on the depth, row, and index.
"""

def find_vect(lst3d, x, y):
    """
    This function takes in a 3D list (lst3d) along with two integers (x and y).
    It then searches for occurrences of x and y at consecutive indices in the 3D list.
    For every occurrence, it records the depth, row, and index in a tuple, all occurrences 
    are stored in the results list which is then returned.
    """
    result = []  # this would hold tuples of depth, row and index

    # We use enumerate to get both index and value as we iterate through the lists
    for depth, lst2d in enumerate(lst3d):
        for row, lst1d in enumerate(lst2d):
            # We only loop till len(lst1d) - 1 because we check lst1d[index + 1] in the loop
            for index in range(len(lst1d) - 1):
                if lst1d[index] == x and lst1d[index + 1] == y:
                    # Record depth, row, index where x and y are found consecutively
                    result.append((depth, row, index))

    # result is automatically sorted as it's inserted in ascending order due to the sequence 
    # of traversal. We don't require a sort method like in C++.

    return result