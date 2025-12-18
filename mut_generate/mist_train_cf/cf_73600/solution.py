"""
QUESTION:
Write a function `longest_common_word` that finds the longest common word among three given paragraphs. The function should return the longest word that appears in all three paragraphs, ignoring case sensitivity and punctuation.
"""

def longest_common_word(paragraph1, paragraph2, paragraph3):
    """
    Finds the longest common word among three given paragraphs, ignoring case sensitivity and punctuation.
    
    Parameters:
    paragraph1 (str): The first paragraph.
    paragraph2 (str): The second paragraph.
    paragraph3 (str): The third paragraph.
    
    Returns:
    str: The longest word that appears in all three paragraphs.
    """
    
    # Convert paragraphs to lower case and remove punctuation
    p1 = ''.join(e for e in paragraph1 if e.isalnum() or e.isspace()).lower()
    p2 = ''.join(e for e in paragraph2 if e.isalnum() or e.isspace()).lower()
    p3 = ''.join(e for e in paragraph3 if e.isalnum() or e.isspace()).lower()
    
    # Split paragraphs into words and convert them to sets
    p1_words = set(p1.split())
    p2_words = set(p2.split())
    p3_words = set(p3.split())
    
    # Find the common words among the three paragraphs
    common_words = p1_words.intersection(p2_words, p3_words)
    
    # Return the longest common word
    return max(common_words, key=len, default='')