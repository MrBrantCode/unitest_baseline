"""
QUESTION:
Analyze the grammatical function of each constituent in a given sentence and categorize them into their respective parts of speech. Implement a function `analyze_sentence` that takes a sentence as input and returns the grammatical analysis.
"""

def analyze_sentence(sentence):
    """
    Analyze the grammatical function of each constituent in a given sentence 
    and categorize them into their respective parts of speech.
    
    Parameters:
    sentence (str): The input sentence to be analyzed.
    
    Returns:
    dict: A dictionary containing the grammatical analysis of the sentence.
    """
    # Tokenize the sentence into words
    tokens = sentence.split()
    
    # Initialize an empty dictionary to store the analysis
    analysis = {}
    
    # Iterate over each token in the sentence
    for i, token in enumerate(tokens):
        # Determine the part of speech for the token
        if token.lower() in ["they", "he", "she", "it"]:
            analysis[token] = "Subject/Personal Pronoun"
        elif token.endswith("ed"):
            analysis[token] = "Main Verb/Simple Past Tense"
        elif token.lower() == "before":
            analysis[token] = "Subordinating Conjunction"
        elif token.endswith("ing"):
            analysis[token] = "Gerund"
        else:
            analysis[token] = "Direct Object/Noun Phrase"
    
    return analysis