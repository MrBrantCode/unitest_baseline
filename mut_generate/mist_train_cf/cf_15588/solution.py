"""
QUESTION:
Create a function `findMissingNum` that finds the smallest positive integer not present in an array. The array can contain both positive and negative numbers. The function should have a time complexity of O(n) and a space complexity of O(1), not using any extra space except for a constant number of variables. If no positive integer is missing, the function should return the smallest positive integer greater than the maximum element in the array.
"""

def findMissingNum(arr):
   """
   This function finds the smallest positive integer not present in an array.
   
   The function iterates through the array to find the maximum positive number, 
   marks visited positive numbers by updating the corresponding index in the array, 
   and then finds the smallest positive integer not present.

   Parameters:
   arr (list): The input array containing both positive and negative numbers.

   Returns:
   int: The smallest positive integer not present in the array.
   """

   # Initialize a variable "maxNum" as 0.
   maxNum = 0
   
   # Iterate through each element "num" in the given array "arr".
   for num in arr:
      # If "num" is positive and greater than "maxNum", update "maxNum" to "num".
      if num > 0 and num > maxNum:
         maxNum = num
   
   # Initialize a variable "missingNum" as "maxNum + 1".
   missingNum = maxNum + 1
   
   # Iterate through each element "num" in the given array "arr" again.
   for num in arr:
      # If "num" is positive and less than or equal to "maxNum", update "arr[num - 1]" to -1 to mark it as visited.
      if num > 0 and num <= maxNum:
         arr[num - 1] = -1
   
   # Iterate through the given array "arr" again.
   for i in range(len(arr)):
      # If any element "num" is greater than 0, return the index of that element plus 1 as the missing number.
      if arr[i] > 0:
         return i + 1
   
   # Return "missingNum" as the smallest positive integer not present in the array.
   return missingNum