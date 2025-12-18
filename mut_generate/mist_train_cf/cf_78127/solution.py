"""
QUESTION:
Define a function `is_mammal` that takes a variable `x` as input and returns `True` if `x` is classified as a mammal, given that every creature is fundamentally classified as a mammal. The function should implement the first-order logic statement ∀x Creature(x) -> Mammal(x).
"""

def is_mammal(x):
  # Assuming 'creatures' is a predefined list of creatures
  for creature in creatures:
    if creature == x:
      return True
  return False