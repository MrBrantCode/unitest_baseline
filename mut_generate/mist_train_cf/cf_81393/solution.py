"""
QUESTION:
Write a Python function `count_char_freq` that takes a string as an input parameter and returns a dictionary. The keys of the dictionary should include the distinct alphabets present in the input string with their respective frequencies, and two additional keys: 'vowels' and 'consonants'. The values for 'vowels' and 'consonants' should represent the cumulative frequency sums of all vowel and consonant letters in the string, respectively. The function should handle both upper and lower-case letters.
"""

def count_char_freq(str):
    # Define the vowels list
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Initialize the dictionary with vowels and consonants
    freq_dict = {'vowels': 0, 'consonants': 0}
    
    for char in str:
        # Check if the character is a letter
        if char.isalpha():
            # Convert to lowercase
            char = char.lower()
            
            # Update the frequency count
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
            
            # Update the vowels and consonants count
            if char in vowels:
                freq_dict['vowels'] += 1
            else:
                freq_dict['consonants'] += 1
    
    # Return the frequency dictionary
    return freq_dict