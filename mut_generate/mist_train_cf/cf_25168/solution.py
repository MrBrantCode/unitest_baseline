"""
QUESTION:
Implement a function named `sort_array` that sorts an array of numbers in ascending order. The input is an array of numbers and the output should be a sorted array of numbers. The function should modify the original array to be in ascending order.
"""

def sort_array(numbers):
    # Bubble sort algorithm 
    for i in range(len(numbers)): 
      for j in range(0, len(numbers)-i-1): 
        if numbers[j] > numbers[j+1]: 
          numbers[j], numbers[j+1] = numbers[j+1], numbers[j] 
    return numbers