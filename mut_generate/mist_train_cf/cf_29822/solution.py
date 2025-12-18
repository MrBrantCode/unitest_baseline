"""
QUESTION:
Create a function `extract_icon_variants(icons)` that takes a list of theme icon dictionaries `icons` as input, where each dictionary contains the icon details, including "icon", "variant", "gradient", and "size". The function should return a dictionary containing unique combinations of icon variants and their corresponding gradient colors. The keys of the dictionary should be the unique icon variants, and the values should be lists of unique gradient color combinations associated with each variant.
"""

def extract_icon_variants(icons):
    unique_variants = {}
    for icon in icons:
        variant = icon["variant"]
        gradient = icon["gradient"]
        if variant in unique_variants:
            if gradient not in unique_variants[variant]:
                unique_variants[variant].append(gradient)
        else:
            unique_variants[variant] = [gradient]
    return unique_variants