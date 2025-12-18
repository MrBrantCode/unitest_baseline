"""
QUESTION:
Create a function named `filter_keywords` that takes two parameters: a string `text` and a list of strings `keywords`. Remove all occurrences of the keywords from the text, regardless of case, and return the resulting string. The function should have a time complexity of O(n * m * k) and a space complexity of O(n), where n is the length of the text, m is the number of keywords, and k is the length of each keyword. The output string should maintain the same case as the input text, and partial matches of keywords should be removed.
"""

def filter_keywords(text, keywords):
    # Convert the input text to lowercase for case-insensitive matching
    text_lower = text.lower()
    # Initialize an empty result string
    result = ""
    # Initialize a dictionary to keep track of removed keywords
    removed_keywords = {}
    
    # Iterate over each character in the text
    i = 0
    while i < len(text):
        # Check if the current character is a potential start of a keyword
        if text_lower[i] in {keyword[0].lower() for keyword in keywords}:
            # Iterate over each keyword
            for keyword in keywords:
                # Check if the current keyword matches the remaining text
                if text_lower[i:i+len(keyword)].startswith(keyword.lower()):
                    # Add the keyword to the removed_keywords dictionary
                    removed_keywords[keyword] = True
                    # Move the index to the end of the keyword
                    i += len(keyword)
                    break
            else:
                # If no keyword match was found, add the current character to the result string
                result += text[i]
                i += 1
        else:
            # If the current character is not the start of a keyword, add it to the result string
            result += text[i]
            i += 1
    
    # Remove the removed keywords from the result string
    for keyword in removed_keywords.keys():
        result = result.replace(keyword, "")
    
    return result