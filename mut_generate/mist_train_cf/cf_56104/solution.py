"""
QUESTION:
Given two lists `A` and `B` where `B` is an anagram of `A` with lengths in the range `[1, 100]` and elements in the range `[0, 10^5]`, write a function `anagramMapping` that returns an index mapping `P` from `A` to `B` where `P[i] = j` means the `i`th element in `A` appears in `B` at index `j`, and the frequency of each element in `P` matches the frequency of the corresponding element in `A`.
"""

def anagramMapping(A, B):
  index_dict = {}
  for i, b in enumerate(B):
      if b not in index_dict:
          index_dict[b] = [i]
      else:
          index_dict[b].append(i)

  result = []
  for a in A:
      result.append(index_dict[a].pop(0))
  
  return result