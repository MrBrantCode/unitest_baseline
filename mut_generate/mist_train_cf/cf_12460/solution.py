"""
QUESTION:
Construct a function named `build_syntax_tree` that takes a sentence as input and returns its corresponding syntax tree representation as a nested dictionary or a custom tree data structure. The function should be able to parse complex sentences with multiple clauses and phrases, and correctly represent the relationships between different words and phrases. The output tree structure may vary depending on the specific conventions used, but it should clearly depict the syntactic relationships between the words and phrases in the input sentence.
"""

def build_syntax_tree(sentence):
    """
    Construct a syntax tree representation of a given sentence.

    Args:
        sentence (str): The input sentence to parse.

    Returns:
        dict: A nested dictionary representing the syntax tree.
    """
    # Tokenize the sentence into words
    words = sentence.split()

    # Initialize the tree with the sentence as the root
    tree = {"label": "ROOT", "children": []}

    # Iterate over the words and build the tree
    for word in words:
        # Assuming a very basic syntax tree structure for simplicity
        # In a real-world scenario, you would use a more sophisticated parsing approach
        if word in ["likes", "eats"]:
            # Create a new node for the verb
            verb_node = {"label": word, "children": []}
            tree["children"].append(verb_node)
        elif word in ["to", "from"]:
            # Create a new node for the preposition
            prep_node = {"label": word, "children": []}
            tree["children"].append(prep_node)
        else:
            # Create a new node for the noun or adjective
            node = {"label": word, "children": []}
            tree["children"].append(node)

    return tree