"""
QUESTION:
Create a function named `calculate_expenditures` that takes nine parameters: `V_tank_m3`, `Inv_a`, `Inv_b`, `Inv_c`, `Inv_d`, `Inv_e`, `Inv_IR`, `Inv_LT`, and `Inv_OM`. Using the given mathematical model, calculate and return the initial capital expenditure (`Capex_a`) and fixed operational expenditure (`Opex_fixed`). The model involves natural logarithm function denoted by `log`.
"""

import math

def calculate_expenditures(V_tank_m3, Inv_a, Inv_b, Inv_c, Inv_d, Inv_e, Inv_IR, Inv_LT, Inv_OM):
    InvC = Inv_a + Inv_b * (V_tank_m3) ** Inv_c + (Inv_d + Inv_e * V_tank_m3) * math.log(V_tank_m3)
    Capex_a = InvC * (Inv_IR) * (1 + Inv_IR) ** Inv_LT / ((1 + Inv_IR) ** Inv_LT - 1)
    Opex_fixed = Capex_a * Inv_OM
    return Capex_a, Opex_fixed