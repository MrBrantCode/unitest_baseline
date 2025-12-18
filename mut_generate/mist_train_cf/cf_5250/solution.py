"""
QUESTION:
Write a function called `analyze_sentence_structure` that takes a list of (word, part-of-speech) pairs as input, where the part-of-speech tags are in Penn Treebank tag format, and returns a string describing the sentence structure, including whether it is a simple sentence, compound sentence, complex sentence, or compound-complex sentence.
"""

def analyze_sentence_structure(pos_tags):
    # Implement your own logic to identify sentence structure
    # You can use pos_tags to analyze dependencies and relationships between words
    # This is a simple example, you might need to extend it further depending on your specific requirements
    
    # Identify coordinating conjunctions (CC), subordinating conjunctions (IN), and verbs (VB)
    coordinating_conjunctions = [tag for word, tag in pos_tags if tag == 'CC']
    subordinating_conjunctions = [tag for word, tag in pos_tags if tag == 'IN']
    verbs = [tag for word, tag in pos_tags if tag.startswith('VB')]
    
    # Determine the sentence structure
    if len(coordinating_conjunctions) > 0 and len(subordinating_conjunctions) > 0:
        return "Compound-Complex Sentence"
    elif len(coordinating_conjunctions) > 0:
        return "Compound Sentence"
    elif len(subordinating_conjunctions) > 0:
        return "Complex Sentence"
    elif len(verbs) == 1:
        return "Simple Sentence"
    else:
        return "Unknown Sentence Structure"