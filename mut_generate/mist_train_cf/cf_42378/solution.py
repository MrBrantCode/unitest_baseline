"""
QUESTION:
Implement the function `process_input(info, probthres, threspv, FDRDict)` that takes a list of strings `info`, a float `probthres`, an integer `threspv`, and a dictionary `FDRDict` as input. The function should check if the 7th element of `info` is less than or equal to `probthres` and the 8th element is less than or equal to 10 raised to the power of negative `threspv`. If the conditions are met and the 8th element is greater than 0, calculate `fdrlevel` using `FDRDict` and the base-10 logarithm of the 8th element, then insert `fdrlevel` as the 9th element of `info`. If the 8th element is 0 or negative, use a predefined value from `FDRDict` and insert it as the 9th element. Finally, return the modified `info` list as a tab-separated string.
"""

import math

def process_input(info, probthres, threspv, FDRDict):
    if float(info[6]) <= probthres and float(info[7]) <= pow(10, -threspv):
        if float(info[7]) > 0:
            fdrlevel = FDRDict[math.floor(-math.log10(float(info[7])) - 0.5)]
        else:
            fdrlevel = FDRDict[-1]
        info.insert(8, str(fdrlevel))
        return '\t'.join(info)
    else:
        return '\t'.join(info)