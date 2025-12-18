"""
QUESTION:
Extract a date from a sentence in the format "Month Day Year" and convert the day into Roman numerals in four standard formats: basic (I, II, III, IV, V, VI, VII, VIII, IX, X), overline (I̅, II̅, III̅, IV̅, V̅, VI̅, VII̅, VIII̅, IX̅, X̅), parentheses ((I), (II), (III), (IV), (V), (VI), (VII), (VIII), (IX), (X)), and periods (I., II., III., IV., V., VI., VII., VIII., IX., X.). 

Implement four functions: `to_roman_basic`, `to_roman_overline`, `to_roman_parentheses`, and `to_roman_period`, each taking an integer day as input and returning its Roman numeral representation in the corresponding format.
"""

def to_roman_basic(num):
    roman = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    return roman[num]

def to_roman_overline(num):
    roman = ["", "I̅", "II̅", "III̅", "IV̅", "V̅", "VI̅", "VII̅", "VIII̅", "IX̅", "X̅"]
    return roman[num]

def to_roman_parentheses(num):
    roman = ["", "(I)", "(II)", "(III)", "(IV)", "(V)", "(VI)", "(VII)", "(VIII)", "(IX)", "(X)"]
    return roman[num]

def to_roman_period(num):
    roman = ["", "I.", "II.", "III.", "IV.", "V.", "VI.", "VII.", "VIII.", "IX.", "X."]
    return roman[num]