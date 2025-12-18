"""
QUESTION:
Implement a function `printer_simulation(strings)` that takes a list of 12 strings and rearranges them into a single string with the first 6 strings concatenated together, followed by a space, and then the remaining 6 strings concatenated together.
"""

def printer_simulation(strings):
    end1, end2, end3, end4, end5, end6 = strings[:6]
    end7, end8, end9, end10, end11, end12 = strings[6:]
    rearranged_string = end1 + end2 + end3 + end4 + end5 + end6 + ' ' + end7 + end8 + end9 + end10 + end11 + end12
    return rearranged_string