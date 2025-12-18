"""
QUESTION:
Write a function `remove_redundancies(seq)` that takes a list of integers as input, removes any repeated elements and non-consecutive integers that do not fit the Fibonacci-like formation (where every number after the first two is the sum of the two preceding ones), and returns the resulting list. The function should not mutate the input list while iterating over it.
"""

def remove_redundancies(seq):
  new_seq = []
  for i in range(len(seq)):
    if i == 0 or i == 1:
      new_seq.append(seq[i])
    else:
      if seq[i] == new_seq[-1] + new_seq[-2] and seq[i] != new_seq[-1]:
        new_seq.append(seq[i])
  return new_seq