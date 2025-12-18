"""
QUESTION:
Create a function called `is_angry(sentence)` that takes a string input `sentence` and returns a boolean indicating whether the sentence contains any phrases indicative of anger. The function should be case-insensitive and consider the following phrases as indicative of anger: "angry", "enraged", "aggrieved", "ineluctably", "ireful", "lusty", "tedious", "vexed", "irked", "wrath".
"""

def is_angry(sentence): 
    angry_phrases = ["angry", "enraged", "aggrieved", "ineluctably", "ireful", 
                    "lusty", "tedious", "vexed", "irked", "wrath"] 
    words_in_sentence = sentence.lower().split(" ")

    for phrase in angry_phrases: 
        if phrase in words_in_sentence: 
            return True 
    return False