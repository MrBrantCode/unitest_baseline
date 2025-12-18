"""
QUESTION:
Write a function named `FindName` that takes two arguments: a list of unique names (`nameList`) and a target name (`targetName`). The function should return the position of `targetName` in `nameList` if it exists (with the first name being at position 1), otherwise it should return 0. The function must handle cases where `targetName` is not in `nameList`.
"""

def FindName(nameList, targetName):
  if targetName in nameList:
    return nameList.index(targetName) + 1  
  else:
    return 0