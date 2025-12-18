"""
QUESTION:
Given the moleculer mass of two molecules ( __M1__ and __M2__ ), their masses present ( __m1__ and __m2__ ) in a vessel of volume ( __V__ ) at a specific temperature ( __T__ ). Find the total pressure exerted by the molecules ( __Ptotal__ ) .

input
====

Six values : 

- __m1__
- __m2__
- __M1__
- __M2__
- __V__
- __T__

output
==== 

One value : 

- __Ptotal__ 

notes
====

Units for each of the following are given as under : 

- _m1_ = gram 
- _m2_ = gram
- _M1_ = _gram.mole^(-1)_
- _M2_ = _gram.mole^(-1)_
- _V_             = _dm^(3)_
- _T_             = Celsius
- __Ptotal__ = atmpspheric pressure (_atm_)

Remember : Temperature is given in Celsius while SI unit is Kelvin (_K_)

0 Celsius = 273.15Kelvin

The gas constant (_R_) has value of _0.082dm^(3).atm.K^(-1).mol^(-1)_
"""

def calculate_total_pressure(m1, m2, M1, M2, V, T):
    """
    Calculate the total pressure exerted by two molecules in a vessel.

    Parameters:
    m1 (float): Mass of the first molecule in grams.
    m2 (float): Mass of the second molecule in grams.
    M1 (float): Molecular mass of the first molecule in grams per mole.
    M2 (float): Molecular mass of the second molecule in grams per mole.
    V (float): Volume of the vessel in cubic decimeters (dm³).
    T (float): Temperature in Celsius.

    Returns:
    float: Total pressure exerted by the molecules in atmospheric pressure (atm).
    """
    # Convert temperature from Celsius to Kelvin
    T_kelvin = T + 273.15
    
    # Calculate the total pressure using the ideal gas law
    Ptotal = (m1 / M1 + m2 / M2) * 0.082 * T_kelvin / V
    
    return Ptotal