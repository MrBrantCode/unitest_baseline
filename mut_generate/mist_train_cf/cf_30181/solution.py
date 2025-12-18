"""
QUESTION:
Write a function `parseFirearmData` that takes a list of strings representing firearm data in the format "CUP_<manufacturer>_<model>_<caliber>_<barrel_length>_<attachment>" and returns a dictionary where the keys are manufacturers and the values are lists of tuples containing the model, caliber, barrel length, and attachment for each firearm. The barrel length and attachment components may have multiple values, but the function should only use the first value if there are multiple.
"""

def parseFirearmData(firearm_strings):
    firearm_data = {}
    for firearm in firearm_strings:
        parts = firearm.split('_')
        manufacturer = parts[1]
        model = parts[2]
        caliber = parts[3]
        barrel_length = parts[4]
        attachment = parts[5] if len(parts) > 5 else None
        if manufacturer in firearm_data:
            firearm_data[manufacturer].append((model, caliber, barrel_length, attachment))
        else:
            firearm_data[manufacturer] = [(model, caliber, barrel_length, attachment)]
    return firearm_data