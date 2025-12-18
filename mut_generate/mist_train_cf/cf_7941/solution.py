"""
QUESTION:
Write a function `remove_element(lst, element)` that takes a list `lst` and an element `x` as input, removes all occurrences of `x` from `lst` while maintaining the original order of the remaining elements, and returns the updated list. The function should have a time complexity of O(n), where n is the length of the list. If `x` is not present in the list, the function should print an error message "Element not found in the list" and return the original list.
"""

def remove_element(lst, element):
  if element not in lst:
    print("Element not found in the list")
    return lst
  
  new_lst = []
  for item in lst:
    if item != element:
      new_lst.append(item)
  
  return new_lst