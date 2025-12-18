"""
QUESTION:
Implement a method `detectLanguage` in a class, which takes a text string and a dictionary of languages with their corresponding confidence levels, where each language's confidence level is determined by a dictionary of language-specific words and their weights. The method should return the language with the highest confidence level based on the input text.
"""

def detectLanguage(text, language_confidences):
    # Split the text into words
    words = text.split()

    # Calculate confidence level for each language
    confidences = {}
    for lang in language_confidences:
        confidence = 0
        for word in words:
            confidence += text.lower().count(word) * language_confidences[lang].get(word, 0)
        confidences[lang] = confidence

    # Determine the language with the highest confidence level
    detected_lang = max(confidences, key=confidences.get)

    return detected_lang