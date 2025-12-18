"""
QUESTION:
You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. The depth of an integer is one plus the maximum depth of the list that contains it. Return the sum of each integer in `nestedList` multiplied by its depth.

`1 <= nestedList.length <= 50`. The values of the integers in the nested list is in the range `[-100, 100]`. The maximum depth of any integer is less than or equal to `50`.
"""

def depthSumInverse(nestedList):
  def getDepth(nestedList, depth):
    maxDepth = depth
    for i in nestedList:
      if isinstance(i, list):
        maxDepth = max(maxDepth, getDepth(i, depth + 1))
    return maxDepth

  def helper(nestedList, depth):
    total = 0
    for i in nestedList:
      if isinstance(i, list):
        total += helper(i, depth - 1)
      else:
        total += i * depth
    return total

  maxDepth = getDepth(nestedList, 1)
  return helper(nestedList, maxDepth)