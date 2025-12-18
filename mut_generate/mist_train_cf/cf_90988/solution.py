"""
QUESTION:
Create a function named `find_common_elements` that takes two lists `list1` and `list2` as parameters and returns a new list containing the elements that are common to both lists. The function should not use built-in functions like `set` or `intersection` to find common elements. It should instead use a loop to iterate over each element in `list1` and check if it exists in `list2`. The common elements should be appended to the result list in the order they appear in `list1`.
"""

def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements