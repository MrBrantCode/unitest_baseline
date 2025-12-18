"""
QUESTION:
Implement a function `processBinaryExpression` that takes in four parameters: an object `obj`, a keyword `keyword`, an operand `operand`, and a modifier `modifier`. The function should perform a specific operation based on the given keyword and return the result of the operation or a success message. The function should support the following keywords: `setvariable`, `setvectordir`, `setvectordirandup`, `setvectorup`, `setvehicleammo`, `setvehicleammodef`, `setvehiclearmor`, `setvehiclecargo`, `setvehicleid`, and `setvehiclelock`. If the keyword is not recognized, the function should return an "Invalid keyword" message.
"""

def processBinaryExpression(obj, keyword, operand, modifier):
    if keyword == 'setvariable':
        obj.variable = operand
        return f"Variable set to {operand} for {obj}"
    elif keyword == 'setvectordir':
        obj.set_direction_vector(operand)
        return f"Direction vector set for {obj}"
    elif keyword == 'setvectordirandup':
        obj.set_direction_and_up_vectors(operand)
        return f"Direction and up vectors set for {obj}"
    elif keyword == 'setvectorup':
        obj.set_up_vector(operand)
        return f"Up vector set for {obj}"
    elif keyword == 'setvehicleammo':
        obj.set_ammo_count(operand)
        return f"Ammunition count set for {obj}"
    elif keyword == 'setvehicleammodef':
        obj.set_ammo_defense(operand)
        return f"Ammunition defense set for {obj}"
    elif keyword == 'setvehiclearmor':
        obj.set_armor_value(operand)
        return f"Armor value set for {obj}"
    elif keyword == 'setvehiclecargo':
        obj.set_cargo(operand, modifier)
        return f"Cargo set for {obj}"
    elif keyword == 'setvehicleid':
        obj.set_id(operand)
        return f"ID set for {obj}"
    elif keyword == 'setvehiclelock':
        obj.set_lock_status(operand)
        return f"Lock status set for {obj}"
    else:
        return "Invalid keyword"