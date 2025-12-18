"""
QUESTION:
Write a function to convert a given integer to Roman Numerals in four standard formats: basic (I, II, III, IV, V, VI, VII, VIII, IX, X), overline (I̅, II̅, III̅, IV̅, V̅, VI̅, VII̅, VIII̅, IX̅, X̅), parentheses ((I), (II), (III), (IV), (V), (VI), (VII), (VIII), (IX), (X)), and periods (I., II., III., IV., V., VI., VII., VIII., IX., X.). The function should take an integer between 1 and 10 as input and return a list of four strings representing the Roman Numerals in each format.
"""

def roman_numerals(num):
    basic = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    overline = ["", "I̅", "II̅", "III̅", "IV̅", "V̅", "VI̅", "VII̅", "VIII̅", "IX̅", "X̅"]
    parentheses = ["", "(I)", "(II)", "(III)", "(IV)", "(V)", "(VI)", "(VII)", "(VIII)", "(IX)", "(X)"]
    period = ["", "I.", "II.", "III.", "IV.", "V.", "VI.", "VII.", "VIII.", "IX.", "X."]
    
    return [basic[num], overline[num], parentheses[num], period[num]]