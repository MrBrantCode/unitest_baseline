"""
QUESTION:
Write a function `mixed_to_improper` that takes a list of mixed fractions as strings in the format 'whole numerator/denominator' and returns a list of their corresponding improper fractions as strings in the format 'numerator/denominator'. The function should handle both positive and negative mixed fractions.
"""

def mixed_to_improper(mixed_fractions):
    improper_fractions = []
    for fraction in mixed_fractions:
        parts = fraction.split()
        whole = int(parts[0])
        numerator, denominator = map(int, parts[1].split('/'))
        if whole < 0:
            numerator = -numerator + (abs(whole) * denominator)
        else:
            numerator = numerator + (whole * denominator)
        improper_fractions.append(f"{numerator}/{denominator}")
    return improper_fractions