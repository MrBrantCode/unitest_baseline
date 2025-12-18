"""
QUESTION:
Write a function called `novel_y_combinator` in Python that implements a novel Y combinator. The novel Y combinator should modify the original Y combinator to prevent infinite recursion in strict evaluation settings by delaying recursion through lambda abstraction.
"""

def novel_y_combinator(f):
    """A novel Y combinator that prevents infinite recursion in strict evaluation settings."""
    
    # Define the delayed recursion through lambda abstraction
    def delayed_recursion(x):
        return lambda v: x(x)(v)
    
    # Define the fixed-point combinator
    def fixpoint_combinator(x):
        return f(delayed_recursion(x))
    
    # Return the result of the fixed-point combinator applied to itself
    return (lambda x: x(x))(fixpoint_combinator)