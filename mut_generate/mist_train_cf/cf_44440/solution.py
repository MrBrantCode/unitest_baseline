"""
QUESTION:
Write a function `locate_sequence(T, q)` that locates the first appearing position of a specific sequence `q` in text data `T`, its count, and creates a dictionary where keys are positions at which `q` appears in `T`, and values are words from `T` that contain the said sequence `q` at that exact position. The function should handle large scale inputs efficiently in terms of time and space complexity.
"""

def locate_sequence(T, q):
    words = T.split()
    first_pos = -1
    count = 0
    dict_positions = {}
    
    for word in words:
        idx = word.find(q)
        if idx != -1:
            if first_pos == -1:
                first_pos = idx
            count += 1
            if idx in dict_positions:
                dict_positions[idx].append(word)
            else:
                dict_positions[idx] = [word]
    
    return first_pos, count, dict_positions