"""
QUESTION:
Create a function named `remove_element` that takes two parameters: a list `lst` and an element `element`. The function should remove all occurrences of `element` from `lst`, maintain the original order of the remaining elements, and return the updated list. If `element` is not present in `lst`, the function should print an error message and return the original list. The solution should have a time complexity of O(n), where n is the length of the list.
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