"""
QUESTION:
Create a function named XNOR that takes two boolean inputs A and B and returns True if A and B are the same (both True or both False), using only the NOR and AND gates. Implement this function in Python using the given NOR and AND functions. The XNOR function should not directly use any other logical operators except the given NOR and AND functions.
"""

def XNOR(A, B):
    def NOR(x, y):
      return not(x or y)

    def AND(x, y):
      return x and y

    N1 = NOR(A, A)
    N2 = NOR(B, B)
    return AND(N1, N2)