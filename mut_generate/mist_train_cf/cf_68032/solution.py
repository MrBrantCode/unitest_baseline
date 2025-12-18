"""
QUESTION:
Write a function `analyse_names(names)` that filters a list of names based on the following conditions: 
1. The name should have more than 4 alphabetic characters.
2. If a name meets the first condition, truncate it to its first 4 characters.
3. Return a list of the modified names that contain at least one vowel.
"""

def analyse_names(names):
    # Vowels in English
    vowels = "aeiou"
    
    # Store the modified names with at least one vowel
    final_names = []
    
    for name in names:
        # If the length of name exceeds 4 alphabetic characters
        if len(name) > 4:
            # Modify the name to include only its first four characters
            modified_name = name[:4].lower()
            
            # Check if the modified name contains at least one vowel
            if any(vowel in modified_name for vowel in vowels):
                # If so, append the name to the final names list
                final_names.append(modified_name)

    return final_names