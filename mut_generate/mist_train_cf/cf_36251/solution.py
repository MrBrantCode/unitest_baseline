"""
QUESTION:
Write a Python function `get_thermo_property(input_type)` that takes a string `input_type` as input, representing a thermodynamic property input type, and returns the corresponding thermodynamic property. The input types and their corresponding thermodynamic properties are as follows:
- PT_INPUTS: Pressure and Temperature
- DmassT_INPUTS: Density and Temperature for mass-based properties
- DmolarT_INPUTS: Density and Temperature for molar-based properties
- HmolarT_INPUTS: Enthalpy and Temperature for molar-based properties
- HmassT_INPUTS: Enthalpy and Temperature for mass-based properties
- SmolarT_INPUTS: Entropy and Temperature for molar-based properties
- SmassT_INPUTS: Entropy and Temperature for mass-based properties

If the input type is not found, the function should return "Invalid input type".
"""

def entance(input_type):
    thermo_properties = {
        'PT_INPUTS': 'Pressure and Temperature',
        'DmassT_INPUTS': 'Density and Temperature for mass-based properties',
        'DmolarT_INPUTS': 'Density and Temperature for molar-based properties',
        'HmolarT_INPUTS': 'Enthalpy and Temperature for molar-based properties',
        'HmassT_INPUTS': 'Enthalpy and Temperature for mass-based properties',
        'SmolarT_INPUTS': 'Entropy and Temperature for molar-based properties',
        'SmassT_INPUTS': 'Entropy and Temperature for mass-based properties'
    }
    
    return thermo_properties.get(input_type, 'Invalid input type')