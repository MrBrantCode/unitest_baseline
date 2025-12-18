"""
QUESTION:
Write a function `closest_number(nums, number)` that finds the closest number in the given list of integers `nums` to the given integer `number`. The function should return the closest number from the list.
"""

def closest_number(nums, number):
  min_diff = abs(nums[0] - number)
  min_num = nums[0]
  for num in nums:
    min_diff_temp = abs(num - number)
    if min_diff_temp < min_diff:
    	min_diff = min_diff_temp
    	min_num = num
  return min_num