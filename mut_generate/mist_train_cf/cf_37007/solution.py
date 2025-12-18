"""
QUESTION:
Create a function called `swap_translations` that takes a dictionary `translations` as input, where the keys are English terms and the values are their corresponding French translations. The function should return a new dictionary with the keys and values swapped. If multiple English terms have the same French translation, the function should append a unique identifier to the French translation to differentiate them.
"""

def swap_translations(translations):
    swapped_translations = {}
    french_to_english = {}
    
    for english, french in translations.items():
        if french in french_to_english:
            french_to_english[french].append(english)
        else:
            french_to_english[french] = [english]
    
    for french, english_list in french_to_english.items():
        if len(english_list) > 1:
            for i, english in enumerate(english_list):
                swapped_translations[french + '_' + str(i+1)] = english
        else:
            swapped_translations[french] = english_list[0]
    
    return swapped_translations