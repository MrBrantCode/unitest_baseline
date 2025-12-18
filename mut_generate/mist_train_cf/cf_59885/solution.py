"""
QUESTION:
Implement the function `sub_in_order` that takes two parameters: `sub_pairs` and `contexts`. `sub_pairs` is a list of tuples where each tuple contains two distinct character sequences, `string1` and `string2`, representing the original sequence and the substitution sequence, respectively. `contexts` is a list of strings where the substitution should take place. The function should substitute the inaugural occurrence of `string1` with `string2` in each context, considering the order of substitution pairs. The function should return a list of updated contexts after all substitutions have been made.
"""

def sub_in_order(sub_pairs, contexts):
  for pair in sub_pairs:
    for i, context in enumerate(contexts):
      contexts[i] = context.replace(pair[0], pair[1], 1)
  return contexts