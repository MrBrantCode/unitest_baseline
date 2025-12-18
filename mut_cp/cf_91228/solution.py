"""
ORIGINAL QUESTION:
Create a function `format_sentence` that takes a list of strings as input. The function should join the strings into a single sentence, following these rules: 
- The first string should be in lowercase, the second in uppercase, the third in lowercase, and so on, alternating between cases.
- Any strings containing vowels (both lowercase and uppercase) should be omitted from the sentence.
- The output sentence should have each word separated by a space.
"""

def format_sentence(strings):
    """
    Formats a list of strings into a sentence, alternating between lowercase and uppercase,
    and omitting strings containing vowels.

    Args:
        strings (list): A list of strings.

    Returns:
        str: The formatted sentence.
    """
    
    # Filter out strings containing vowels
    filtered_words = [word for word in strings if not any(vowel in word.lower() for vowel in "aeiou")]

    # Convert the strings to lowercase or uppercase based on their index
    formatted_words = [filtered_words[i].lower() if i % 2 == 0 else filtered_words[i].upper() for i in range(len(filtered_words))]

    # Join the formatted words into a single sentence
    sentence = " ".join(formatted_words)

    return sentence