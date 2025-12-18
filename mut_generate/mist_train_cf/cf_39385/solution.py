"""
QUESTION:
Implement a function `ocr_decode` that takes a 2D NumPy array `log_probs` of shape (T, C) representing log probabilities of each character at each time step and an integer `beam_width` as input, and returns the decoded sequence as a string using the prefix beam search algorithm with the given beam width.
"""

def ocr_decode(log_probs, beam_width):
    T, C = log_probs.shape
    initial_beam = [((), 0)]  
    for t in range(T):  
        new_beam = {}  
        for prefix, score in initial_beam:  
            for c in range(C):  
                new_prefix = prefix + (c,)  
                new_score = score + log_probs[t, c]  
                new_beam[new_prefix] = new_score  
        initial_beam = sorted(new_beam.items(), key=lambda x: x[1], reverse=True)[:beam_width]  
    best_sequence = max(initial_beam, key=lambda x: x[1])[0]  
    decoded_sequence = ''.join(map(str, best_sequence))  
    return decoded_sequence