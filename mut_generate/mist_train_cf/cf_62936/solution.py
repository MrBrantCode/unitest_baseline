"""
QUESTION:
Write a function `final_instance_position(S, P)` that finds the last overlapping instance of pattern `P` within string `S`. The function should consider overlapping patterns and be case-sensitive. If `P` does not occur in `S`, the function should return -1.
"""

def final_instance_position(S, P):
   '''Find the last overlapping instance of P in S'''
   positions = [i for i in range(len(S)) if S.startswith(P, i)]
   if positions:
       return positions[-1]
   else:
       return -1