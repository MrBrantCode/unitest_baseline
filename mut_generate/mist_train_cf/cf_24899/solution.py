"""
QUESTION:
Design a function `detectInfiniteLoop(program)` that takes a string of newline-separated program instructions as input and returns True if the program contains an infinite loop (i.e., a repeated instruction) and False otherwise.
"""

def detectInfiniteLoop(program):
  setOfInstructions = set()
  for line in program.split('\n'):
    if line in setOfInstructions:
      return True
    setOfInstructions.add(line)
  return False