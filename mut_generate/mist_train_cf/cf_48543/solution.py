"""
QUESTION:
Implement a function named `will_it_fly(q, w)` that takes a sequence `q` and a weight limit `w` as inputs. The function should return `True` if the sequence `q` is palindromic and its total weight does not exceed `w`, and `False` otherwise. The function should also handle error cases: return `"Non-numeric input"` if `q` contains non-numeric elements, and `"Non-sequence input"` if `q` is not a sequence.
"""

def will_it_fly(q, w):
    '''
    The function's purpose is to discern q's flight potential, return True if achievable, and False if not. For q to fly, it must fulfil two prerequisites: it must be palindromic and the total weights of its elements should not go beyond the maximum acceptable weight w.

    Implement the function with error handling mechanisms. It should return a "Non-numeric input" error if it receives a non-numeric input, and a "Non-sequence input" error if it receives a non-sequence input.
    '''
    # Handle Non-sequence input error
    if not isinstance(q, (list, tuple, str)):
        return "Non-sequence input"
    
    for i in q:
        # Handle Non-numeric input error
        if not isinstance(i, (int, float)):
            return "Non-numeric input"
    
    return q == q[::-1] and sum(q) <= w