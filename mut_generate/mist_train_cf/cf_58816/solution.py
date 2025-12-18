"""
QUESTION:
Write two functions, `recursive` and `iterative`, that take two parameters `start` and `end` to calculate the total sum of all values between `start` and `end` (inclusive). 

Restrictions: 
- Both `start` and `end` must be non-negative integers.
- `start` must not exceed `end`.
- The functions should handle invalid inputs and provide suitable error messages.
- Compare the time and space complexity of both functions and discuss their advantages and disadvantages.
- Provide test cases to validate the results.
"""

def recursive(start, end):
  if not(isinstance(start, int) and isinstance(end, int)):
    return "Both inputs must be integers."
  elif start < 0 or end < 0:
    return "Inputs must be non-negative."
  elif start > end:
    return "Start value must not exceed end value."
  elif end <= start:
    return start
  else:
    return end + recursive(start, end-1)

def iterative(start, end):
  if not(isinstance(start, int) and isinstance(end, int)):
    return "Both inputs must be integers."
  elif start < 0 or end < 0:
    return "Inputs must be non-negative."
  elif start > end:
    return "Start value must not exceed end value."
  else:
    result = 0
    for i in range(start, end+1):
      result += i
    return result