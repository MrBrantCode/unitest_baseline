"""
QUESTION:
Create a function called `tri_split` that takes a list of names as input and returns three lists of names. The names should be divided into three groups based on their first letter, with the first group containing names that start with letters 'a' to 'g', the second group containing names that start with letters 'h' to 'p', and the third group containing names that start with letters 'q' to 'z'. The function should handle names with different cases and should not modify the original list.
"""

def tri_split(names):
    names.sort()  # sorting the names
    group1, group2, group3 = [], [], []  # initialization of empty groups

    for name in names:
        if ord(name[0].lower()) < ord('h'):  # if initial character is less than 'h'
            group1.append(name)
        elif ord('h') <= ord(name[0].lower()) < ord('q'):  # if initial character is between 'h' and 'p'
            group2.append(name)
        else:  # If initial character is greater than 'p'
            group3.append(name)

    return group1, group2, group3