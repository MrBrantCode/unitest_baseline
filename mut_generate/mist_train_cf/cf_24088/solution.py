"""
QUESTION:
Write a function named `find_pairs(nums, sum)` that takes a list of integers `nums` and a target sum as input, and returns all pairs of numbers in the list whose sum equals the target sum. The function should not return duplicate pairs and the pairs should be in the order they appear in the input list. The input list may contain duplicate numbers and the function should treat them as distinct numbers.
"""

def find_pairs(nums, sum):
  """
  This function finds all pairs of numbers in the list whose sum equals the target sum.

  Args:
    nums (list): A list of integers.
    sum (int): The target sum.

  Returns:
    list: A list of tuples, where each tuple contains a pair of numbers that sum up to the target sum.
  """
  result = set()
  pairs = []
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == sum and (nums[j], nums[i]) not in result:
        result.add((nums[i], nums[j]))
        pairs.append((nums[i], nums[j]))
  return pairs