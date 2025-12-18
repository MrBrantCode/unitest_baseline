"""
QUESTION:
Create a function `organize_plug_types(plug_list)` that takes a list of strings representing different types of electrical plugs in the format "standard-voltage-phase-connector-amperage" and returns a dictionary. The dictionary should have tuples representing the characteristics (voltage, phase, connector) in that order as keys and lists of plug types that match the characteristics represented by the key as values. 

The function should only consider the voltage, phase, and connector for the key, ignoring the standard and amperage. If the voltage, phase, or connector is missing from the string, it should be represented as an empty string in the key.
"""

def organize_plug_types(plug_list):
    plug_dict = {}
    for plug in plug_list:
        parts = plug.split("-")
        voltage = parts[1].split("V")[0]
        phase = parts[2]
        connector = parts[3]
        key = (voltage, phase, connector)
        if key in plug_dict:
            plug_dict[key].append(plug)
        else:
            plug_dict[key] = [plug]
    return plug_dict