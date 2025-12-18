"""
QUESTION:
Filter out unwanted words from a given paragraph of text, ignoring case sensitivity. The function should take two parameters: a string paragraph and a dictionary of language-specific unwanted words where each key is a language code and its corresponding value is a set of unwanted words. The function should return the filtered paragraph after removing the unwanted words. The algorithm should be efficient, handling large input sizes and avoiding excessive use of built-in string manipulation functions. It should also support multiple languages by detecting the language of the paragraph based on the occurrence of common words in each language.
"""

def filter_unwanted_words(paragraph, unwanted_words):
    """
    Filter out unwanted words from a given paragraph of text, ignoring case sensitivity.
    
    Parameters:
    paragraph (str): The input paragraph to be filtered.
    unwanted_words (dict): A dictionary of language-specific unwanted words where each key is a language code and its corresponding value is a set of unwanted words.
    
    Returns:
    str: The filtered paragraph after removing the unwanted words.
    """

    # Language Detection
    common_words = {
        'en': {'the', 'and', 'a', 'of', 'to'},  # Add more common words for each language
        'es': {'de', 'la', 'que', 'el', 'en'},  # Add more common words for each language
        # Add more languages as needed
    }

    words = paragraph.split()
    language_counts = {lang: sum(1 for word in words if word.lower() in common_words[lang]) for lang in common_words}
    detected_language = max(language_counts, key=language_counts.get)

    # Filtering
    filtered_words = []
    unwanted_words_set = set(unwanted_words.get(detected_language, set()))
    
    for word in words:
        if word.lower() not in unwanted_words_set:
            filtered_words.append(word)
    
    return ' '.join(filtered_words)