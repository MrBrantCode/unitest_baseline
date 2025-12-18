"""
QUESTION:
Write a function `compare_civilizations` that compares the technological progress of two civilizations. The function takes two `ThreeBodyCivilization` objects as input and only performs the comparison if both civilizations have a non-zero level of technology and are not hostile towards each other. If the civilizations have the same technology level, the function should indicate that they are equal.
"""

class ThreeBodyCivilization:
    def __init__(self, name, technology_level, is_hostile):
        self.name = name
        self.technology_level = technology_level
        self.is_hostile = is_hostile

def compare_civilizations(civ1, civ2):
    # check if both civilizations have a non-zero level of technology
    if civ1.technology_level == 0 or civ2.technology_level == 0:
        return "One or both civilizations have a zero level of technology."

    # check if the civilizations are hostile towards each other
    if civ1.is_hostile or civ2.is_hostile:
        return "The civilizations are hostile towards each other."

    # compare the technology levels of the two civilizations
    if civ1.technology_level > civ2.technology_level:
        return f"{civ1.name} is more technologically advanced than {civ2.name}"
    elif civ1.technology_level < civ2.technology_level:
        return f"{civ2.name} is more technologically advanced than {civ1.name}"
    else:
        return "Both civilizations are equally technologically advanced."