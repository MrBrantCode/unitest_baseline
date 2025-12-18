"""
QUESTION:
Given the ratios of daps to yaps and yaps to baps, write a function named `calculate_original_unit` that calculates the original unit in daps given a certain number of baps. The function should take three parameters: `daps_yaps_ratio` (a list of two integers representing the ratio of daps to yaps), `yaps_baps_ratio` (a list of two integers representing the ratio of yaps to baps), and `given_baps` (the given number of baps).
"""

def calculate_original_unit(daps_yaps_ratio, yaps_baps_ratio, given_baps):
    # convert ratios to float for precision
    daps_yaps_ratio = [float(i) for i in daps_yaps_ratio]
    yaps_baps_ratio = [float(i) for i in yaps_baps_ratio]
    # calculate dap-bap ratio
    daps_baps_ratio = (daps_yaps_ratio[0]/daps_yaps_ratio[1]) * (yaps_baps_ratio[0]/yaps_baps_ratio[1])
    # calculate original unit
    original_unit_daps = given_baps * daps_baps_ratio
    return original_unit_daps