"""
QUESTION:
Create a function `find_position(node)` that takes a node from a bi-directional linked list as input and returns the numerical position of that node from its position to the end of the list. The function should start traversing from the given node, not from the head of the list.
"""

def find_position(node):
  """
  This function takes a node from a bi-directional linked list as input and returns 
  the numerical position of that node from its position to the end of the list.

  Args:
    node (Node): A node from a bi-directional linked list.

  Returns:
    int: The numerical position of the node from its position to the end of the list.
  """
  temp = node
  position = 0
  while temp:
    temp = temp.next
    position += 1
  return position