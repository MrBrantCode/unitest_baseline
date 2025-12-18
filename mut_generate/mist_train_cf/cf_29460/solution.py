"""
QUESTION:
Write a function `chemicalReaction(c, o)` that takes in the initial quantities of carbon (c) and oxygen (o) as parameters and returns the final quantities of carbon and oxygen after a reaction. The reaction occurs if the amount of carbon is at least half of the amount of oxygen, consuming half of the oxygen molecules and an equal number of carbon molecules. If the reaction cannot occur, the function should return the original quantities of carbon and oxygen. The function should return a tuple of two integers. The input parameters are integers representing the initial quantities of carbon and oxygen.
"""

from typing import Tuple

def chemicalReaction(c: int, o: int) -> Tuple[int, int]:
    if 2 * c >= o:  
        co2 = o // 2  
        c -= co2  
        o -= co2*2  
    return c, o 