"""
QUESTION:
Write a function called `toTheOrdinal(num, isFeminine)` that takes an integer `num` between 1 and 99 and a boolean `isFeminine` as input and returns the ordinal representation of the number in French. The function should return the ordinal representation in the format "Le <number>ème" if `isFeminine` is False, and "La <number>ème" if `isFeminine` is True.
"""

def toTheOrdinal(num, isFeminine=False):
    """
    Returns the ordinal representation of the number in French.

    Args:
        num (int): An integer between 1 and 99.
        isFeminine (bool, optional): Whether the ordinal should be feminine. Defaults to False.

    Returns:
        str: The ordinal representation of the number in French.
    """
    ordinals = {
        1: "premier" if not isFeminine else "première",
        2: "deuxième" if not isFeminine else "deuxième",
        3: "troisième" if not isFeminine else "troisième",
        4: "quatrième" if not isFeminine else "quatrième",
        5: "cinquième" if not isFeminine else "cinquième",
        6: "sixième" if not isFeminine else "sixième",
        7: "septième" if not isFeminine else "septième",
        8: "huitième" if not isFeminine else "huitième",
        9: "neuvième" if not isFeminine else "neuvième",
        10: "dixième" if not isFeminine else "dixième",
        11: "onzième" if not isFeminine else "onzième",
        12: "douzième" if not isFeminine else "douzième",
        13: "treizième" if not isFeminine else "treizième",
        14: "quatorzième" if not isFeminine else "quatorzième",
        15: "quinzième" if not isFeminine else "quinzième",
        16: "seizième" if not isFeminine else "seizième",
        17: "dix-septième" if not isFeminine else "dix-septième",
        18: "dix-huitième" if not isFeminine else "dix-huitième",
        19: "dix-neuvième" if not isFeminine else "dix-neuvième",
        20: "vingtième" if not isFeminine else "vingtième",
        30: "trentième" if not isFeminine else "trentième",
        40: "quarantième" if not isFeminine else "quarantième",
        50: "cinquantième" if not isFeminine else "cinquantième",
        60: "soixantième" if not isFeminine else "soixantième",
        70: "soixante-dixième" if not isFeminine else "soixante-dixième",
        80: "quatre-vingtième" if not isFeminine else "quatre-vingtième",
        90: "quatre-vingt-dixième" if not isFeminine else "quatre-vingt-dixième",
    }

    if num in ordinals:
        return f"{'Le' if not isFeminine else 'La'} {ordinals[num]}"
    else:
        tens = (num // 10) * 10
        units = num % 10
        return f"{'Le' if not isFeminine else 'La'} {ordinals[tens]}-{ordinals[units]}"