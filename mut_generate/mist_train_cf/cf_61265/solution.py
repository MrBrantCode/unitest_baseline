"""
QUESTION:
Develop a function named `sort_list` that takes a list of values (`givenList`) and a string specifying the sort order (`sortOrder`) as input. The function should sort the integers in the list in the specified order (either "ascending" or "descending"), exclude any non-integer values, and return the sorted list of integers. If non-integer values are found, the function should print an error message indicating the detected non-integer values before returning the sorted list.
"""

def sort_list(givenList, sortOrder):
  """
  Sorts a list of integers in a specified order while excluding non-integer values.

  Args:
    givenList (list): A list containing integers and possibly other data types.
    sortOrder (str): The desired order of sorting. It can be either "ascending" or "descending".

  Returns:
    list: A sorted list of integers.

  Raises:
    None
  """
  nonIntegers = [i for i in givenList if not isinstance(i, int)]
  if nonIntegers:
    print(f"Non-integer values detected: {nonIntegers}. These values will be excluded from the sorted list.")
  integerList = [i for i in givenList if isinstance(i, int)]
  sortedList = sorted(integerList, reverse = (sortOrder == "descending"))
  return sortedList