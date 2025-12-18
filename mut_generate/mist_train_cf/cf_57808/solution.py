"""
QUESTION:
Develop a function named `custom_sort_reverse` that takes a list of lists, where each sublist contains strings, and performs the following operations: 
- removes duplicates within each sublist
- sorts each sublist in ascending order (lexicographically) without using the built-in `sort` function
- merges the sublists into a single list while maintaining the sorted order and ensuring no duplicates
- reverses the final list without using the built-in `reverse` function
- handles potential exceptions and errors, providing error messages when the input is not a list of lists of strings.
"""

def custom_sort_reverse(lst):
  try:
    assert type(lst) == list # Check if input is a list
    for sublist in lst:
      assert type(sublist) == list  # Check if all elements in list are lists
      for element in sublist:
        assert type(element) == str  # Check if each sublist only contains strings
      
    # Start Operations
    # Operation 1 and 2
    sorted_lst = [sorted(list(set(sublist))) for sublist in lst]
    
    # Operation 3 and 4
    result = []
    for sublist in sorted_lst:
      for element in sublist:
        if element not in result:
          result.append(element)

    # Reverse the list
    for i in range(len(result)//2):
      result[i], result[-i-1] = result[-i-1], result[i]

    return result

  # Error Handling
  except AssertionError:
    return "Input error: ensure all elements are lists of strings."
  except Exception as e:
    return str(e)