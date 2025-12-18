"""
QUESTION:
Create a function called `superior_frequency_map` that takes a string `test` as input. The function should create a frequency map of all characters in the string, interpreting uppercase and lowercase letters as equivalent, and including numerical digits and orthographic symbols. The function should return a dictionary where the keys are the unique characters in the string and the values are their corresponding frequencies.
"""

def superior_frequency_map(test: str):
  frequency = {}
  for c in test.lower():
      if c in frequency:
          frequency[c] +=1
      else:
          frequency[c] =1
  return frequency