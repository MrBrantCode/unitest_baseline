"""
QUESTION:
Implement a function, so it will produce a sentence out of the given parts.

Array of parts could contain:
- words;
- commas in the middle;
- multiple periods at the end.

Sentence making rules:
- there must always be a space between words;
- there must not be a space between a comma and word on the left;
- there must always be one and only one period at the end of a sentence.

**Example:**
"""

def construct_sentence(parts):
    # Join the parts with a space
    sentence = ' '.join(parts)
    
    # Remove spaces before commas
    sentence = sentence.replace(' ,', ',')
    
    # Strip any leading/trailing spaces and periods
    sentence = sentence.strip(' .')
    
    # Ensure there is exactly one period at the end
    return sentence + '.'