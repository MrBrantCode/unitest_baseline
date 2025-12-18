"""
QUESTION:
How to make a cake you'll never eat.

Ingredients. 

  * 2 carrots
  * 0 calories
  * 100 g chocolate spread
  * 1 pack of flour
  * 1 egg



Method. 

  1. Put calories into the mixing bowl.
  2. Take carrots from refrigerator.
  3. Chop carrots.
  4. Take chocolate spread from refrigerator.
  5. Put chocolate spread into the mixing bowl.
  6. Combine pack of flour into the mixing bowl.
  7. Fold chocolate spread into the mixing bowl.
  8. Add chocolate spread into the mixing bowl.
  9. Put pack of flour into the mixing bowl.
  10. Add egg into the mixing bowl.
  11. Fold pack of flour into the mixing bowl.
  12. Chop carrots until choped.
  13. Pour contents of the mixing bowl into the baking dish.



Serves 1.

Input

The only line of input contains a sequence of integers a0, a1, ... (1 ≤ a0 ≤ 100, 0 ≤ ai ≤ 1000 for i ≥ 1).

Output

Output a single integer.

Examples

Input

4 1 2 3 4


Output

30
"""

def compute_cake_value(sequence: list[int]) -> int:
    """
    Computes the value of the cake based on the given sequence of integers.

    Parameters:
    sequence (list[int]): A list of integers where the first element (a0) indicates the number of elements to process,
                          and the subsequent elements (a1, a2, ...) are used in the computation.

    Returns:
    int: The computed value based on the given sequence.
    """
    a0 = sequence[0]
    s = 0
    for i in range(a0):
        s += (i + 1) * sequence[i + 1]
    return s