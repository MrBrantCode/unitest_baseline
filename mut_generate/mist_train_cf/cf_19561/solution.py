"""
QUESTION:
Create a function called `find_element` that takes a list and an element as input, and returns the index of the element in the list if it exists, otherwise returns -1. Implement the function using a for loop or a while loop to iterate through the list and find the element. The function should not use any built-in list methods to find the index of the element.
"""

def find_element(lst, elem):
    found = False
    index = 0
    for i in lst:
        if i == elem:
            found = True
            index = lst.index(i)
            break
        else:
            index += 1
    if found == False:
        return -1
    else:
        return index