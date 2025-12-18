"""
QUESTION:
Create a function named `calc_weighted_mean` that calculates the weighted mean of a list of numbers and their corresponding weights. The function should take two lists as input, `nums` and `weights`, and return the weighted mean as a number. If `nums` and `weights` are not of equal length, the function should return an error message.
"""

def calc_weighted_mean(nums, weights):
   if len(nums) != len(weights):
      return "The lists of numbers and weights are not of equal length."
   
   weighted_sum = sum(num * weight for num, weight in zip(nums, weights))
   total_weights = sum(weights)
   
   return weighted_sum / total_weights