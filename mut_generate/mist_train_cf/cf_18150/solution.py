"""
QUESTION:
Create a function `filter_keywords(text, keywords)` that takes two parameters: a string `text` of length `n` containing only alphabetical characters and spaces, and a list `keywords` of `m` strings, each of length `k`. The function should return a new string that is formed by removing all occurrences of the keywords from the input text in a case-insensitive manner, including partial matches. The order of the keywords in the output string should be the same as their order in the input list. The function should have a time complexity of O(n * m * k) and a space complexity of O(n).
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