"""
QUESTION:
Create a function named `to_roman` that takes an integer as input and returns its Roman numeral representation in four standard formats: Basic (I, II, III, IV, V, VI, VII, VIII, IX, X), Overline (I̅, II̅, III̅, IV̅, V̅, VI̅, VII̅, VIII̅, IX̅, X̅), Parentheses ((I), (II), (III), (IV), (V), (VI), (VII), (VIII), (IX), (X)), and Period (I., II., III., IV., V., VI., VII., VIII., IX., X.). The function should handle integers from 1 to 10.
"""

def to_roman(num):
    """
    Returns the Roman numeral representation of the input integer in four standard formats.
    
    Parameters:
    num (int): The input integer to be converted to Roman numerals.
    
    Returns:
    dict: A dictionary containing the Roman numeral representations in basic, overline, parentheses, and period formats.
    """
    roman_basic = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    roman_overline = ["", "I̅", "II̅", "III̅", "IV̅", "V̅", "VI̅", "VII̅", "VIII̅", "IX̅", "X̅"]
    roman_parentheses = ["", "(I)", "(II)", "(III)", "(IV)", "(V)", "(VI)", "(VII)", "(VIII)", "(IX)", "(X)"]
    roman_period = ["", "I.", "II.", "III.", "IV.", "V.", "VI.", "VII.", "VIII.", "IX.", "X."]
    
    return {
        "basic": roman_basic[num],
        "overline": roman_overline[num],
        "parentheses": roman_parentheses[num],
        "period": roman_period[num]
    }