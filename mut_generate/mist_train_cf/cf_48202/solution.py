"""
QUESTION:
Implement the `entityParser` function to parse HTML entities in a given text string. The function should replace all entities of special characters with their corresponding symbols. The special characters and their entities are: `&quot;` for Quotation Mark, `&apos;` for Single Quote Mark, `&amp;` for Ampersand, `&gt;` for Greater Than Sign, `&lt;` for Less Than Sign, and `&frasl;` for Slash. The function should handle nested entities and replace them correctly. The input `text` string length is between 1 and 10^6 and can contain any possible ASCII characters. The function should return the text after replacing the entities by the special characters.
"""

def entityParser(text):
    mp = {"&quot;": '"', "&apos;": "'", "&amp;": '&', "&gt;": '>', "&lt;": '<', "&frasl;": '/'}
    for key in mp.keys():
        text = text.replace(key, mp[key])
    return text